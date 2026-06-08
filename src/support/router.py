from fastapi import APIRouter, Depends

from src.support.dependencies import get_support_service
from src.support.schemas import SupportRequest, SupportResponse
from src.support.service import SupportService

router = APIRouter(
    prefix="/support",
    tags=["Support"],
)


@router.post("/ask", response_model=SupportResponse)
def ask_support(
    request: SupportRequest,
    support_service: SupportService = Depends(get_support_service),
) -> SupportResponse:
    answer = support_service.generate_support_answer(request)
    return SupportResponse(
        ticket_id=request.ticket_id,
        priority=request.priority,
        category=request.category,
        **answer.model_dump(),
    )
