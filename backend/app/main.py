# main.py
print("🔥 AUTH ROUTES LOADED")

from fastapi import FastAPI
from database.db import engine, Base
import database.models
from api.routes.patient_routes import router as patient_router
from api.routes.hospital_routes import router as hospital_router
from api.routes.auth_routes import router as auth_router
from api.routes.triage_routes import router as triage_router
from api.routes.test_routes import router as test_router

# NEW: include ai router
from api.routes.ai_routes import router as ai_router

# Import RAG pipeline (keep if you want direct dev access elsewhere)
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

# Register AI router (this exposes POST /ai-triage expecting JSON body)
app.include_router(ai_router)

@app.get("/")
def root():
    return {"status": "Backend running"}

# NOTE: removed the old inline @app.post("/ai-triage") function that accepted symptoms as a plain str.
# The API surface now uses the typed/modeled route in api.routes.ai_routes.