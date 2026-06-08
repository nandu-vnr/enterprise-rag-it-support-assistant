from functools import lru_cache
from typing import Any, Literal
from pydantic import field_validator, model_validator
from pydantic_settings import BaseSettings, SettingsConfigDict

from src.llm_providers.constants import ChatProvider, EmbeddingProvider
from src.llm_providers.validators import validate_provider_settings


class Settings(BaseSettings):
    # Application Configuration
    PROJECT_NAME: str = "the current project"
    PROJECT_DESCRIPTION: str = "determined by the available sources"

    RAGPI_VERSION: str = "v0.1.0"
    API_NAME: str = "Enterprise RAG Support API"
    API_SUMMARY: str = "RAG-powered assistant for IT support, incident triage, and resolution recommendation."

    RAGPI_API_KEY: str | None = None

    WORKERS_ENABLED: bool = True
    TASK_RETENTION_DAYS: int = 7
    LOG_LEVEL: Literal["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"] = "INFO"
    USER_AGENT: str = "Enterprise RAG IT Support Assistant"
    MAX_CONCURRENT_REQUESTS: int = 10

    CORS_ENABLED: bool = False
    CORS_ORIGINS: list[str] = ["*"]

    # Provider Configuration
    CHAT_PROVIDER: ChatProvider = ChatProvider.OPENAI
    EMBEDDING_PROVIDER: EmbeddingProvider = EmbeddingProvider.OPENAI

    OPENAI_API_KEY: str | None = None

    OLLAMA_BASE_URL: str | None = None

    DEEPSEEK_API_KEY: str | None = None

    CHAT_OPENAI_COMPATIBLE_BASE_URL: str | None = None
    CHAT_OPENAI_COMPATIBLE_API_KEY: str | None = None

    EMBEDDING_OPENAI_COMPATIBLE_BASE_URL: str | None = None
    EMBEDDING_OPENAI_COMPATIBLE_API_KEY: str | None = None

    # Database Configuration
    REDIS_URL: str = "redis://localhost:6379"
    POSTGRES_URL: str = (
        "postgresql://localhost:5432/enterprise_rag_it_support_assistant"  # Assumes a local Postgres db named 'enterprise_rag_it_support_assistant' exists
    )
    POSTGRES_POOL_SIZE: int = 10
    POSTGRES_MAX_OVERFLOW: int = 10
    POSTGRES_POOL_RECYCLE: int = 1800

    DOCUMENT_STORE_BACKEND: Literal["postgres", "redis"] = "postgres"
    DOCUMENT_STORE_NAMESPACE: str = "document_store"

    SOURCE_METADATA_BACKEND: Literal["postgres", "redis"] = "postgres"
    SOURCE_METADATA_NAMESPACE: str = "source_metadata"

    # Chat Settings
    BASE_SYSTEM_PROMPT: str = (
        "You are an AI assistant specialized in retrieving and synthesizing technical information to provide relevant answers to queries."
    )
    CHAT_HISTORY_LIMIT: int = 20
    MAX_CHAT_ITERATIONS: int = 5
    RETRIEVAL_TOP_K: int = 10

    # Model Settings
    DEFAULT_CHAT_MODEL: str = "gpt-4o"
    EMBEDDING_MODEL: str = "text-embedding-3-small"
    EMBEDDING_DIMENSIONS: int = 768  # Default for text-embedding-3-small model

    # GitHub
    GITHUB_TOKEN: str | None = None
    GITHUB_API_VERSION: str = "2022-11-28"

    # Document Processing
    DOCUMENT_UUID_NAMESPACE: str = "ee747eb2-fd0f-4650-9785-a2e9ae036ff2"
    CHUNK_SIZE: int = 512
    CHUNK_OVERLAP: int = 50
    DOCUMENT_SYNC_BATCH_SIZE: int = 500

    # OpenTelemetry Settings
    OTEL_ENABLED: bool = False
    OTEL_SERVICE_NAME: str = "enterprise-rag-it-support-assistant"

    @model_validator(mode="after")
    def validate_llm_providers(self):
        return validate_provider_settings(self)

    @field_validator("LOG_LEVEL", mode="before")
    def normalize_log_level(cls, v: Any):
        if isinstance(v, str):
            return v.upper()
        return v

    @field_validator("CORS_ORIGINS", mode="before")
    def validate_list_from_string(cls, v: Any):
        if isinstance(v, str):
            return [item.strip() for item in v.split(",")]
        return v

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


@lru_cache
def get_settings():
    return Settings()
