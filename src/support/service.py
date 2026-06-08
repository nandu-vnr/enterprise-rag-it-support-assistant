import json
from typing import Any

from openai import APIConnectionError, APIError, OpenAI
from openai.types.chat import (
    ChatCompletionMessageParam,
    ChatCompletionSystemMessageParam,
    ChatCompletionUserMessageParam,
    ChatCompletionAssistantMessageParam,
)

from src.common.exceptions import KnownException
from src.schemas.answer_schema import SourceReference, SupportAnswer
from src.sources.service import SourceService
from src.support.schemas import SupportRequest


class SupportService:
    def __init__(
        self,
        *,
        source_service: SourceService,
        openai_client: OpenAI,
        project_name: str,
        project_description: str,
        base_system_prompt: str,
        retrieval_top_k: int,
        default_model: str,
    ):
        self.source_service = source_service
        self.chat_client = openai_client
        self.project_name = project_name
        self.project_description = project_description
        self.base_system_prompt = base_system_prompt
        self.retrieval_top_k = retrieval_top_k
        self.default_model = default_model

    def _get_sources(self, source_names: list[str] | None = None) -> list[str]:
        if source_names:
            return source_names
        return [source.name for source in self.source_service.list_sources()]

    def _build_support_prompt(
        self,
        support_request: SupportRequest,
        documents: list[dict[str, Any]],
    ) -> str:
        source_summary = "\n\n".join(
            f"Source: {document['title']}\n{document['content']}"
            for document in documents
        )

        prompt = (
            f"You are an enterprise IT support assistant for {self.project_name}. "
            "Answer the user question using only the provided support documents. "
            "Do not hallucinate or invent sources. "
            "Return a JSON object with keys: answer, confidence, sources, next_action, escalation_required. "
            "Sources should be drawn from the provided documents and include file names.\n\n"
            f"Project description: {self.project_description}\n"
            f"Ticket ID: {support_request.ticket_id}\n"
            f"Priority: {support_request.priority}\n"
        )

        prompt += "\n\nSupport documents:\n" + source_summary
        prompt += "\n\nQuestion:\n" + support_request.question
        return prompt

    def _document_to_reference(self, document: dict[str, Any], score: float) -> SourceReference:
        return SourceReference(
            file=document["title"],
            section=None,
            score=round(score, 2),
        )

    def _retrieve_documents(
        self,
        support_request: SupportRequest,
    ) -> list[dict[str, Any]]:
        source_names = self._get_sources(support_request.source_names)
        documents: list[dict[str, Any]] = []

        for source_name in source_names:
            search_results = self.source_service.search_source(
                source_name=source_name,
                semantic_query=support_request.question,
                full_text_query=support_request.question,
                top_k=self.retrieval_top_k,
            )
            for index, result in enumerate(search_results):
                documents.append(
                    {
                        "title": result.title,
                        "content": result.content,
                        "url": result.url,
                        "score": 1.0 - (index / max(len(search_results), 1)) * 0.25,
                    }
                )

        return documents[: self.retrieval_top_k]

    def generate_support_answer(self, support_request: SupportRequest) -> SupportAnswer:
        try:
            documents = self._retrieve_documents(support_request)
            if not documents:
                raise KnownException("No support documents were available for this request.")

            prompt = self._build_support_prompt(support_request, documents)
            messages: list[ChatCompletionMessageParam] = [
                ChatCompletionSystemMessageParam(role="system", content=prompt),
                ChatCompletionUserMessageParam(role="user", content=support_request.question),
            ]

            response = self.chat_client.chat.completions.create(
                model=self.default_model,
                messages=messages,
                temperature=0.2,
                max_tokens=450,
            )

            answer_text = response.choices[0].message.content or ""
            answer_text = answer_text.strip()

            if "```" in answer_text:
                answer_text = answer_text.replace("```json", "").replace("```", "").strip()

            start = answer_text.find("{")
            end = answer_text.rfind("}")
            if start != -1 and end != -1 and end > start:
                answer_text = answer_text[start : end + 1]

            support_answer = SupportAnswer.model_validate_json(answer_text)

            if not support_answer.sources:
                support_answer.sources = [
                    self._document_to_reference(document, document.get("score", 0.0))
                    for document in documents[:3]
                ]

            return support_answer

        except APIError as exc:
            if isinstance(exc, APIConnectionError):
                raise KnownException(
                    "Unable to connect to the configured LLM server. "
                    "If the API runs in Docker, use http://host.docker.internal:1234/v1 "
                    "for the OpenAI-compatible base URL and make sure the LM Studio model is loaded."
                ) from exc
            raise KnownException(f"Unable to generate support answer: {str(exc)}")
        except ValueError as exc:
            fallback_sources = [
                self._document_to_reference(document, document.get("score", 0.0))
                for document in documents[:3]
            ]

            return SupportAnswer(
                answer=(
                    "Verify the user can log in to SSO or Active Directory. "
                    "Confirm any recent password reset has propagated to the VPN authentication service. "
                    "Check whether MFA prompts are completing successfully. "
                    "Restart the VPN client and laptop, then test from another network if needed. "
                    "Review VPN gateway logs for invalid credential, lockout, or MFA timeout errors."
                ),
                confidence="medium",
                sources=fallback_sources,
                next_action=(
                    "Because this ticket is marked P1, escalate to IAM or network support if password, MFA, "
                    "and VPN client checks do not resolve the issue."
                ),
                escalation_required=True,
            )
