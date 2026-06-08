import pytest

from src.config import Settings
from src.connectors.connector_type import ConnectorType
from src.connectors.exceptions import ConnectorException
from src.connectors.local_markdown.config import LocalMarkdownConfig
from src.connectors.local_markdown.connector import LocalMarkdownConnector


@pytest.mark.asyncio
async def test_extract_local_markdown_files(tmp_path) -> None:
    docs_root = tmp_path / "data" / "raw"
    runbooks_dir = docs_root / "runbooks"
    incidents_dir = docs_root / "incidents"
    runbooks_dir.mkdir(parents=True)
    incidents_dir.mkdir(parents=True)

    (runbooks_dir / "database_runbook.md").write_text(
        "# Database Runbook\n\nUse this document for database troubleshooting.",
        encoding="utf-8",
    )
    (incidents_dir / "database_incident.md").write_text(
        "# Database Incident\n\nThe database was timing out.",
        encoding="utf-8",
    )
    (docs_root / "ignore.txt").write_text("not markdown", encoding="utf-8")

    settings = Settings(OPENAI_API_KEY="test-key", CHUNK_SIZE=512, CHUNK_OVERLAP=0)
    config = LocalMarkdownConfig(
        type=ConnectorType.LOCAL_MARKDOWN,
        root_path=str(docs_root),
    )
    connector = LocalMarkdownConnector(settings=settings, config=config)

    documents = [doc async for doc in connector.extract()]

    assert len(documents) == 2
    assert all(doc.url.startswith("file://") for doc in documents)
    assert any("Database Runbook" in doc.title for doc in documents)
    assert any("Database Incident" in doc.title for doc in documents)


@pytest.mark.asyncio
async def test_extract_local_markdown_missing_root_path() -> None:
    settings = Settings(OPENAI_API_KEY="test-key")
    config = LocalMarkdownConfig(
        type=ConnectorType.LOCAL_MARKDOWN,
        root_path="/does/not/exist",
    )
    connector = LocalMarkdownConnector(settings=settings, config=config)

    with pytest.raises(ConnectorException):
        [doc async for doc in connector.extract()]
