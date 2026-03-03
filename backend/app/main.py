print("🔥 AUTH ROUTES LOADED")

from fastapi import FastAPI
from database.db import engine
from database.models import Base

from api.routes.patient_routes import router as patient_router
from api.routes.hospital_routes import router as hospital_router
from api.routes.auth_routes import router as auth_router
from api.routes.triage_routes import router as triage_router
from api.routes.test_routes import router as test_router

# Import RAG pipeline
from services.rag_pipeline import rag_query

app = FastAPI()

# Create tables automatically
Base.metadata.create_all(bind=engine)

# Include existing routers
app.include_router(patient_router)
app.include_router(hospital_router)
app.include_router(auth_router)
app.include_router(triage_router)
app.include_router(test_router)


@app.get("/")
def root():
    return {"status": "Backend running"}


# 🔹 AI TRIAGE ENDPOINT (from Person B)
@app.post("/ai-triage")
def ai_triage(symptoms: str):
    result = rag_query(symptoms)
    return {"response": result}
