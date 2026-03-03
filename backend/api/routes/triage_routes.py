from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database.db import get_db
from services.triage_service import run_triage

router = APIRouter(prefix="/triage", tags=["Triage"])

@router.post("/{patient_id}")
def triage_patient(patient_id: str, db: Session = Depends(get_db)):
    return run_triage(db, patient_id)
