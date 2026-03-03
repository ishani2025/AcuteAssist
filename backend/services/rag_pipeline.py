# services/rag_pipeline.py
from services.retrieval_service import retrieve_context
from services.llm_service import ask_llm
import re
from typing import Optional, Dict

def parse_response(resp_text: str) -> Optional[Dict[str, str]]:
    """
    Tolerant parser: accept a few label variants and return normalized dict.
    Returns None if nothing usable found.
    """
    if not resp_text or not resp_text.strip():
        return None

    # Normalize newlines and trim
    lines = [l.strip() for l in resp_text.splitlines() if l.strip()]

    diag, level, action = None, None, None
    for line in lines:
        low = line.lower()
        if low.startswith("diagnosis:") or low.startswith("condition:") or low.startswith("most likely condition:"):
            diag = line.split(":", 1)[1].strip()
        elif low.startswith("emergency_level:") or low.startswith("emergency level:") or ("emergency" in low and any(k in low for k in ["high", "moderate", "low", "critical"])):
            m = re.search(r"(high|moderate|low|critical)", low, re.I)
            if m:
                level = m.group(1).upper()
            else:
                # attempt after colon if present
                level = line.split(":",1)[1].strip() if ":" in line else line
        elif low.startswith("immediate_action:") or low.startswith("immediate action:") or low.startswith("action:"):
            action = line.split(":",1)[1].strip()

    # Fallback: if not all labels found, try three-line free-format (first line diag, second level, third action)
    if not (diag and level and action) and len(lines) >= 3:
        if not diag:
            diag = lines[0]
        if not level:
            level = lines[1]
        if not action:
            action = lines[2]

    if diag or level or action:
        diag = diag or "Unknown"
        level = level or "MODERATE"
        action = action or "Seek medical evaluation."
        return {
            "diagnosis": diag,
            "emergency_level": level,
            "immediate_action": action
        }

    return None


def rag_query(symptoms: str, history: str = None) -> Dict[str, str]:
    context, confidence = retrieve_context(symptoms)

    print("\n==============================")
    print("SYMPTOMS:", symptoms)
    print("RETRIEVED CONTEXT (trimmed):\n", context[:1200])
    print("==============================\n")

    # Prompt unchanged (we are not modifying the model prompt)
    prompt = f"""Patient symptoms:
{symptoms}

Medical information (use only this):
{context}

Respond exactly in three lines:

Diagnosis: <condition>
Emergency_Level: <LOW | MODERATE | HIGH | CRITICAL>
Immediate_Action: <short instruction>
"""

    print("PROMPT SENT TO MODEL:\n", prompt[:1000])

    response = ask_llm(prompt)
    print("RAW LLM RESPONSE:\n", (response or "")[:1000])

    parsed = parse_response(response)
    if parsed:
        return parsed

    # Retry with top chunk if parsing failed
    if context and len(context) > 0:
        short_context = context.split("\n\n")[0]
        retry_prompt = f"""Patient symptoms:
{symptoms}

Medical information (top chunk only):
{short_context}

Respond in three lines:

Diagnosis:
Emergency_Level:
Immediate_Action:
"""
        print("RETRYING WITH TOP CHUNK...")
        response2 = ask_llm(retry_prompt)
        parsed2 = parse_response(response2)
        if parsed2:
            return parsed2

    # final conservative fallback returning dict (consistent shape)
    return {
        "diagnosis": "Unknown",
        "emergency_level": "MODERATE",
        "immediate_action": "Seek medical evaluation."
    }