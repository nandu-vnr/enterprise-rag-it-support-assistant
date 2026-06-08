from pydantic import BaseModel

from src.schemas.answer_schema import SupportAnswer


class SupportRequest(BaseModel):
    ticket_id: str
    question: str
    priority: str
    category: str | None = None
    source_names: list[str] | None = None


class SupportResponse(SupportAnswer):
    ticket_id: str
    priority: str
    category: str | None = None
