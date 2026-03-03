# api/routes/ai_routes.py
from fastapi import APIRouter
from app.schemas.triage_schema import TriageRequest, TriageResponse
from services.rag_pipeline import rag_query

router = APIRouter()

@router.post("/ai-triage", response_model=TriageResponse)
def ai_triage(request: TriageRequest) -> TriageResponse:
    """
    Accepts JSON of shape { "symptoms": "..." } and returns structured JSON:
    { "diagnosis": "...", "emergency_level": "...", "immediate_action": "..." }
    """
    result = rag_query(request.symptoms)
    # result is already a dict with the expected keys (see rag_query changes)
    return result