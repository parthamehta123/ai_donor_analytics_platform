from fastapi import APIRouter, Depends, HTTPException, Query
from app.tools import get_campaign_performance, get_donor_retention
from app.rag.generator import answer
from app.security import require_role
from app.models import CampaignPerformance, DonorRetention, RagResponse

router = APIRouter()


@router.get(
    "/tools/campaign-performance",
    response_model=CampaignPerformance,
    tags=["Tools"],
)
def campaign_performance(
    client_id: str = Query(..., description="Client identifier (e.g. abc, demo, xyz)"),
    _: None = Depends(require_role("analyst")),
):
    result = get_campaign_performance(client_id)

    if hasattr(result, "error"):
        raise HTTPException(status_code=404, detail=result.error)

    return result


@router.get(
    "/tools/donor-retention",
    response_model=DonorRetention,
    tags=["Tools"],
)
def donor_retention(
    client_id: str = Query(..., description="Client identifier"),
    _: None = Depends(require_role("strategist")),
):
    return get_donor_retention(client_id)


@router.get("/rag/ask", response_model=RagResponse, tags=["RAG"])
def rag_query(q: str = Query(..., min_length=5)):
    return {"question": q, "answer": answer(q)}
