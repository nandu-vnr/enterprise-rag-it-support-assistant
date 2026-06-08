from pathlib import Path
from typing import AsyncGenerator
from fnmatch import fnmatch

from src.config import Settings
from src.connectors.base.connector import BaseConnector
from src.connectors.common.chunker import chunk_markdown_page
from src.connectors.common.schemas import ExtractedDocument, MarkdownPage
from src.connectors.exceptions import ConnectorException
from src.connectors.local_markdown.config import LocalMarkdownConfig


class LocalMarkdownConnector(BaseConnector):
    config: LocalMarkdownConfig

    def __init__(self, settings: Settings, config: LocalMarkdownConfig):
        super().__init__(settings, config)

    def _resolve_root_path(self) -> Path:
        root_path = Path(self.config.root_path).expanduser()
        if not root_path.is_absolute():
            root_path = (Path.cwd() / root_path).resolve()
        return root_path

    def _is_excluded(self, relative_path: Path) -> bool:
        if not self.config.exclude_globs:
            return False

        relative_name = relative_path.as_posix()
        return any(fnmatch(relative_name, pattern) for pattern in self.config.exclude_globs)

    async def extract(self) -> AsyncGenerator[ExtractedDocument, None]:
        root_path = self._resolve_root_path()
        if not root_path.exists():
            raise ConnectorException(
                f"Markdown root path does not exist: {root_path}"
            )

        found_files = False
        for file_path in sorted(root_path.glob(self.config.include_glob)):
            if not file_path.is_file():
                continue

            relative_path = file_path.relative_to(root_path)
            if self._is_excluded(relative_path):
                continue

            found_files = True
            content = file_path.read_text(encoding="utf-8")
            page = MarkdownPage(
                url=file_path.resolve().as_uri(),
                title=file_path.stem.replace("_", " ").replace("-", " ").title(),
                content=content,
            )

            chunks = chunk_markdown_page(
                page_data=page,
                chunk_size=self.settings.CHUNK_SIZE,
                chunk_overlap=self.settings.CHUNK_OVERLAP,
            )
            for chunk in chunks:
                yield chunk

        if not found_files:
            raise ConnectorException(
                f"No markdown files found in {root_path} matching {self.config.include_glob}"
            )
