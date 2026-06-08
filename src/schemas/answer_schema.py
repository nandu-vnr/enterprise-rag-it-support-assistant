from typing import List, Literal
from pydantic import BaseModel


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
