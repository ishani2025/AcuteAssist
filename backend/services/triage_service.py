from database.patient_repository import get_patient_by_id
from database.test_repository import get_tests_by_patient
from services.deterministic_filter import extract_clinical_markers

from services.case_router_service import detect_case
from services.case1_service import process_local_history
from services.case2_service import fetch_fragmented_history
from services.context_services import build_context
from services.llm_service import ask_llm
from services.retrieval_service import retrieve_context


async def run_triage(db, symptoms, patient_id=None, aadhaar=None):

    # -------------------------
    # 1. DATABASE CHECK
    # -------------------------
    patient = None
    markers = {}

    if patient_id:
        patient = get_patient_by_id(db, patient_id)

        if patient:
            tests = get_tests_by_patient(db, str(patient_id))
            markers = extract_clinical_markers(tests)

    # -------------------------
    # 2. DETERMINISTIC TRIAGE
    # -------------------------
    risk_level = "LOW"

    if "troponin" in markers and markers["troponin"] > 0.4:
        risk_level = "HIGH"

    elif "blood_pressure" in markers and markers["blood_pressure"] > 180:
        risk_level = "MEDIUM"

    # -------------------------
    # 3. CASE DETECTION
    # -------------------------
    case = await detect_case(patient_id, aadhaar)

    history = None

    if case == "LOCAL_HISTORY":
        history = await process_local_history(["report1.pdf"])

    elif case == "FRAGMENTED_HISTORY":
        history = await fetch_fragmented_history(aadhaar)

    # -------------------------
    # 4. RAG KNOWLEDGE
    # -------------------------
    knowledge = retrieve_context(symptoms)

    context = build_context(symptoms, history, knowledge)

    # -------------------------
    # 5. LLM TRIAGE
    # -------------------------
    ai_result = ask_llm(context)

    # -------------------------
    # 6. FINAL RESPONSE
    # -------------------------
    return {
        "patient_id": patient_id,
        "risk_level": risk_level,
        "markers": markers,
        "ai_triage": ai_result
    }
