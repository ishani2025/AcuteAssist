# services/llm_service.py
import requests

OLLAMA_URL = "http://localhost:11434/api/chat"
MODEL = "mistral:latest"


def ask_llm(prompt):
    payload = {
        "model": MODEL,
        "messages": [
            {"role": "system", "content": "You are an emergency medical triage AI. Keep answers short and only use provided knowledge."},
            {"role": "user", "content": prompt}
        ],
        "stream": False,
        "options": {
            "temperature": 0.2,
            "num_predict": 200
        }
    }

    res = requests.post(OLLAMA_URL, json=payload, timeout=60)
    data = res.json()

    print("\nOLLAMA RAW RESPONSE:\n", data)  # debug: inspect message/content/done flags

    # Robust extraction: some versions return data["message"]["content"], others data["response"]
    # guard against empty / missing content
    message = None
    if "message" in data and isinstance(data["message"], dict):
        message = data["message"].get("content", "")
    if not message:
        message = data.get("response", "")

    return (message or "").strip()