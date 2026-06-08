from fastapi import Depends

from src.config import get_settings, Settings
from src.llm_providers.client import get_chat_openai_client
from src.sources.dependencies import get_source_service
from src.sources.service import SourceService
from src.support.service import SupportService


def get_support_service(
    source_service: SourceService = Depends(get_source_service),
    settings: Settings = Depends(get_settings),
    openai_client = Depends(get_chat_openai_client),
) -> SupportService:
    return SupportService(
        source_service=source_service,
        openai_client=openai_client,
        project_name=settings.PROJECT_NAME,
        project_description=settings.PROJECT_DESCRIPTION,
        base_system_prompt=settings.BASE_SYSTEM_PROMPT,
        retrieval_top_k=settings.RETRIEVAL_TOP_K,
        default_model=settings.DEFAULT_CHAT_MODEL,
    )
