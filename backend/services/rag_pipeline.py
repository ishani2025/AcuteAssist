# services/rag_pipeline.py
from services.retrieval_service import retrieve_context
from services.llm_service import ask_llm
import re

def parse_response(resp_text: str):
    """
    Tolerant parser: accept a few label variants and return normalized string.
    """
    if not resp_text or not resp_text.strip():
        return None

    # Normalize newlines
    lines = [l.strip() for l in resp_text.splitlines() if l.strip()]

    # Try to find Diagnosis / Emergency_Level / Immediate_Action lines
    diag, level, action = None, None, None
    for line in lines:
        low = line.lower()
        if low.startswith("diagnosis:") or low.startswith("condition:") or low.startswith("most likely condition:"):
            diag = line.split(":", 1)[1].strip()
        elif low.startswith("emergency_level:") or low.startswith("emergency level:") or "emergency" in low and any(k in low for k in ["high", "moderate", "low", "critical"]):
            # attempt to extract HIGH/MODERATE/LOW/CRITICAL
            m = re.search(r"(high|moderate|low|critical)", low, re.I)
            if m:
                level = m.group(1).upper()
            else:
                level = line.split(":",1)[1].strip() if ":" in line else line
        elif low.startswith("immediate_action:") or low.startswith("immediate action:") or low.startswith("action:"):
            action = line.split(":",1)[1].strip()

    # Fallback: try three-line free-format (first line diag, second level, third action)
    if not (diag and level and action) and len(lines) >= 3:
        if not diag:
            diag = lines[0]
        if not level:
            level = lines[1]
        if not action:
            action = lines[2]

    if diag or level or action:
        # build clean output string
        diag = diag or "Unknown"
        level = level or "MODERATE"
        action = action or "Seek medical evaluation."
        return f"Diagnosis: {diag}\nEmergency_Level: {level}\nImmediate_Action: {action}"
    return None


def rag_query(symptoms: str, history: str = None):
    context, confidence = retrieve_context(symptoms)

    print("\n==============================")
    print("SYMPTOMS:", symptoms)
    print("RETRIEVED CONTEXT (trimmed):\n", context[:1200])
    print("==============================\n")

    # Minimal, non-noisy prompt (keep it short)
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
    print("RAW LLM RESPONSE:\n", response[:1000])

    parsed = parse_response(response)
    if parsed:
        return parsed

    # If model returned nothing parsed, allow one gentle retry with smaller context (safety)
    # (Avoid long retries in production — this is a quick dev-time resilience step)
    if context and len(context) > 0:
        # try again with single best chunk
        short_context = context.split("\n\n")[0]  # top chunk only
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

    # final conservative fallback (no overwriting real model answers)
    return """Diagnosis: Unknown
Emergency_Level: MODERATE
Immediate_Action: Seek medical evaluation."""