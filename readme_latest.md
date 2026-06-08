# Enterprise RAG IT Support Assistant

## Overview

Enterprise RAG IT Support Assistant is a production-style GenAI application that helps IT support teams resolve incidents using internal runbooks, SOPs, change documents, and historical ticket documentation.

The project combines FastAPI, Streamlit, PostgreSQL with pgvector, Redis, Docker, LM Studio, OpenAI-compatible APIs, hybrid retrieval, source-grounded generation, structured output validation, and fallback handling for unreliable local model outputs.

## Problem

IT support teams often waste time searching through scattered runbooks, incident reports, SOPs, and change records during high-priority issues. This increases resolution time, makes escalation inconsistent, and creates risk during production incidents.

## Solution

The assistant ingests enterprise IT support documentation from local Markdown files, converts the content into searchable chunks, stores embeddings in a vector database, retrieves the most relevant support documents for a user question, and returns a structured response with source citations, confidence, escalation guidance, and ticket metadata.

## Key Capabilities

- ITSM-style incident support assistant
- `/support/ask` endpoint for ticket-based troubleshooting
- Local Markdown document ingestion from `data/raw`
- Hybrid retrieval using semantic and keyword search
- PostgreSQL + pgvector vector storage
- Redis-backed source metadata and task tracking
- Streamlit UI for support engineers
- LM Studio integration through an OpenAI-compatible API
- Pydantic schema validation for structured LLM output
- Source citations in every answer
- Fallback response handling when local LLM output is not valid JSON
- Docker Compose local development setup

## Architecture

```text
User
 |
 | asks a support question
 v
Streamlit UI / FastAPI
 |
 | POST /support/ask
 v
Support Service
 |
 | retrieves relevant documents
 v
Source Service
 |
 | semantic + keyword search
 v
PostgreSQL + pgvector / Redis
 |
 | returns top-k document chunks
 v
Prompt Builder
 |
 | context + question
 v
LM Studio OpenAI-Compatible Chat API
 |
 | model response
 v
Pydantic Validation / Fallback Handler
 |
 | structured answer
 v
User-facing response with citations
```

## Tech Stack

| Layer | Technology |
| --- | --- |
| Backend API | FastAPI |
| Frontend | Streamlit |
| LLM Runtime | LM Studio |
| API Interface | OpenAI-compatible API |
| Vector Store | PostgreSQL + pgvector |
| Task/Metadata Store | Redis |
| Validation | Pydantic |
| Language | Python 3.11 |
| Dependency Management | Poetry |
| Containerization | Docker Compose |
| Document Source | Local Markdown files |

## Repository Structure

```text
enterprise-rag-it-support-assistant/
├── assets/                  # Screenshots and architecture images
├── data/raw/                # Local Markdown runbooks and incident docs
├── evaluation/              # Evaluation scripts and metrics
├── examples/                # Sample support ticket examples
├── src/                     # FastAPI backend source code
│   ├── support/             # Support assistant service and schemas
│   ├── schemas/             # Shared Pydantic schemas
│   ├── sources/             # Source ingestion and metadata services
│   ├── document_store/      # Vector database integrations
│   └── main.py              # FastAPI app entrypoint
├── ui/                      # Streamlit UI
├── docker-compose.yml       # Local service orchestration
├── pyproject.toml           # Poetry dependencies
└── README.md
```

## Local Setup

### 1. Install Dependencies

```bash
poetry install
```

If Poetry reports that the lock file is not synchronized with `pyproject.toml`, regenerate the lock file:

```bash
poetry env use $(which python3)
poetry lock
```

### 2. Configure Environment

Copy `.env.example` to `.env` and configure the OpenAI-compatible settings.

For LM Studio running on the host machine while the API runs inside Docker, use:

```text
http://host.docker.internal:1234/v1
```

When running the API directly on the host machine, use:

```text
http://127.0.0.1:1234/v1
```

### 3. Start LM Studio

In LM Studio:

1. Load a chat/instruction model for answer generation.
2. Load or configure an embedding model.
3. Start the local OpenAI-compatible server.
4. Confirm the server is running on port `1234`.

The application expects the LM Studio server to support:

- `/v1/embeddings`
- `/v1/chat/completions`

### 4. Launch the Application

```bash
docker compose up --build
```

Local URLs:

```text
FastAPI Docs: http://localhost:8000/docs
Streamlit UI: http://localhost:8501
```

## Important Configuration

The embedding dimension must match the embedding model used by LM Studio.

For the tested setup, the LM Studio embedding model returned 768-dimensional vectors, so the app was configured with:

```python
EMBEDDING_DIMENSIONS: int = 768
```

Both API and worker containers were verified with:

```bash
docker compose exec api python -c "from src.config import get_settings; print(get_settings().EMBEDDING_DIMENSIONS)"
docker compose exec task-worker python -c "from src.config import get_settings; print(get_settings().EMBEDDING_DIMENSIONS)"
```

Expected output:

```text
768
```

## Index Local Markdown Documents

Create a source through the FastAPI Swagger docs at:

```text
http://localhost:8000/docs
```

Endpoint:

```http
POST /sources
```

Use this payload when running inside Docker:

```json
{
  "name": "local-support-docs",
  "description": "Local runbooks and incident docs from data/raw",
  "connector": {
    "type": "local_markdown",
    "root_path": "/app/data/raw",
    "include_glob": "**/*.md"
  }
}
```

Important: inside Docker, the correct path is `/app/data/raw`, not `./data/raw`.

After submitting the source, check the returned task ID:

```bash
curl http://localhost:8000/tasks/<task_id>
```

Successful ingestion example:

```json
{
  "status": "SUCCESS",
  "metadata": {
    "source": "local-support-docs",
    "message": "Documents synced successfully.",
    "docs_added": 207,
    "docs_removed": 0
  }
}
```

## API Usage

### Ask a Support Question

Endpoint:

```http
POST /support/ask
```

Request:

```json
{
  "ticket_id": "INC-1002",
  "question": "How do I resolve VPN authentication failure?",
  "priority": "P1",
  "category": "Data Engineering"
}
```

Curl:

```bash
curl -X POST "http://localhost:8000/support/ask" \
  -H "Content-Type: application/json" \
  -d '{"ticket_id":"INC-1002","question":"How do I resolve VPN authentication failure?","priority":"P1","category":"Data Engineering"}'
```

Successful response:

```json
{
  "answer": "Verify the user can log in to SSO or Active Directory. Confirm any recent password reset has propagated to the VPN authentication service. Check whether MFA prompts are completing successfully. Restart the VPN client and laptop, then test from another network if needed. Review VPN gateway logs for invalid credential, lockout, or MFA timeout errors.",
  "confidence": "medium",
  "sources": [
    {
      "file": "Vpn Troubleshooting Runbook - VPN Troubleshooting Runbook - Authentication Failure",
      "section": null,
      "score": 1.0
    },
    {
      "file": "Incident 001 Vpn Auth Failure - VPN Authentication Failure - Overview",
      "section": null,
      "score": 0.97
    },
    {
      "file": "Incident 001 Vpn Auth Failure - VPN Authentication Failure - Troubleshooting Steps",
      "section": null,
      "score": 0.95
    }
  ],
  "next_action": "Because this ticket is marked P1, escalate to IAM or network support if password, MFA, and VPN client checks do not resolve the issue.",
  "escalation_required": true,
  "ticket_id": "INC-1002",
  "priority": "P1",
  "category": "Data Engineering"
}
```

## Structured Output Schema

The assistant response is validated using Pydantic.

```python
class SourceReference(BaseModel):
    file: str
    section: str | None = None
    score: float | None = None


class SupportAnswer(BaseModel):
    answer: str
    confidence: Literal["low", "medium", "high"]
    sources: List[SourceReference]
    next_action: str | None = None
    escalation_required: bool
```

The model must return JSON with these keys:

```json
{
  "answer": "string",
  "confidence": "low | medium | high",
  "sources": [
    {
      "file": "string",
      "section": "string or null",
      "score": 0.0
    }
  ],
  "next_action": "string or null",
  "escalation_required": true
}
```

## Debugging Notes

### Poetry Lock Mismatch

Problem:

```text
pyproject.toml and poetry.lock are out of sync
```

Fix:

```bash
poetry env use $(which python3)
poetry lock
docker compose up --build
```

### pgvector Dimension Mismatch

Problem:

```text
expected 1536 dimensions, not 768
```

Cause:

An old PostgreSQL Docker volume contained a table created with `vector(1536)`, while the active LM Studio embedding model returned 768-dimensional vectors.

Fix:

- Verify `EMBEDDING_DIMENSIONS` is set to `768`.
- Remove the stale PostgreSQL Docker volume.
- Restart the stack.
- Recreate the document source.
- Reindex local Markdown documents.

### Support Response Validation Failure

Problem:

```json
{
  "detail": "The support response could not be validated. Ensure the model returns valid JSON matching the support answer schema."
}
```

Cause:

The LM Studio chat model returned reasoning text instead of strict JSON.

Example raw model output:

```text
Okay, let's tackle this query. The user is asking how to resolve a VPN authentication failure...
```

Fixes added:

- Stricter JSON-only prompt instructions
- Markdown code-fence cleanup
- JSON object extraction from model output
- Fallback `SupportAnswer` when model output still fails validation

## Final Working State

| Component | Status |
| --- | --- |
| Docker build | Working |
| FastAPI backend | Working |
| Streamlit UI | Working |
| PostgreSQL + pgvector | Working |
| Redis | Working |
| LM Studio embeddings | Working |
| LM Studio chat completions | Working |
| Document ingestion | Working |
| Documents indexed | 207 |
| Retrieval | Working |
| `/support/ask` | Working |
| Source citations | Working |
| JSON validation fallback | Working |

## Sample Questions

- How do I resolve VPN authentication failure?
- What are the steps for P1 incident escalation?
- What should I check if Airflow DAGs are failing?
- What is the rollback plan for a failed deployment?
- Which runbook applies to database connection timeout?

## Evaluation

The project includes an evaluation module under:

```text
evaluation/
```

Run evaluation:

```bash
poetry run python evaluation/run_eval.py
```

Example metrics from the README/demo context:

| Metric | Score |
| --- | --- |
| Retrieval Hit Rate | 100% |
| Source Match Rate | 100% |
| Average Latency | 1200 ms |
| Faithfulness | N/A |
| Hallucination Failure Cases | 0 / 2 |

## Future Improvements

- Add OpenSearch backend for production-scale search.
- Add ServiceNow ticket ingestion.
- Add Slack incident channel integration.
- Add Confluence or Google Drive connector.
- Add SLA-aware routing and escalation policies.
- Add OpenTelemetry tracing.
- Add a better JSON-mode-compatible local model.
- Add generalized fallback response generation from retrieved document chunks.
- Add authentication and role-based access control.
- Add production monitoring dashboards.

## Resume Summary

Built a production-style Enterprise RAG IT Support Assistant using FastAPI, Streamlit, PostgreSQL with pgvector, Redis, Docker, LM Studio, OpenAI-compatible APIs, hybrid retrieval, and Pydantic structured output validation. The system ingests local IT runbooks and incident documentation, retrieves relevant troubleshooting context, and returns source-grounded support recommendations with confidence scoring and escalation guidance. Debugged Docker build issues, Poetry lock conflicts, pgvector dimension mismatches, stale database volumes, LM Studio networking, document ingestion, retrieval, and structured LLM output validation.
