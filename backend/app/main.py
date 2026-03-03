from fastapi import FastAPI
from services.rag_pipeline import rag_query

app = FastAPI()

@app.post("/triage")

def triage(symptoms: str):

    result = rag_query(symptoms)

    return {"response": result}