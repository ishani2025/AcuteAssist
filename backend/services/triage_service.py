from services.case_router_service import detect_case
from services.case1_service import process_local_history
from services.case2_service import fetch_fragmented_history
from services.context_services import build_context
from services.llm_service import ask_llm
from services.retrieval_service import retrieve_context

async def run_triage(symptoms, patient_id=None, aadhaar=None):

    case = await detect_case(patient_id, aadhaar)

    history = None

    if case == "LOCAL_HISTORY":
        history = await process_local_history(["report1.pdf"])

    elif case == "FRAGMENTED_HISTORY":
        history = await fetch_fragmented_history(aadhaar)

    knowledge = retrieve_context(symptoms)

    context = build_context(symptoms, history, knowledge)

    result = ask_llm(context)

    return result