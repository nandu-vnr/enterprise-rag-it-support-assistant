from typing import Literal

from pydantic import Field

from src.connectors.base.config import BaseConnectorConfig
from src.connectors.connector_type import ConnectorType


class LocalMarkdownConfig(BaseConnectorConfig):
    """Configuration for a local markdown connector."""

    type: Literal[ConnectorType.LOCAL_MARKDOWN] = Field(
        description="Connector type identifier"
    )
    root_path: str = Field(
        description="Path to the directory that contains markdown files"
    )
    include_glob: str = Field(
        default="**/*.md",
        description="Glob pattern for files to include relative to root_path",
    )
    exclude_globs: list[str] | None = Field(
        default=None,
        description="Optional glob patterns to exclude relative to root_path",
    )
