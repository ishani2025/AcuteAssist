from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from auth.role_checker import require_role

from database.db import get_db
from database.patient_repository import (
    create_patient,
    get_patient_by_id,
    get_all_patients,
)
from models.schemas import PatientCreate, PatientResponse
from auth.jwt_handler import get_current_user

router = APIRouter(prefix="/patients", tags=["Patients"])

@router.post("/", response_model=PatientResponse)
def register_patient(
    patient: PatientCreate,
    db: Session = Depends(get_db),
    current_user = Depends(require_role("receptionist"))
):
    return create_patient(db, patient.dict())

# 🔐 Fetch Single Patient (Any Logged-In User)
@router.get("/{patient_id}", response_model=PatientResponse)
def fetch_patient(
    patient_id: str,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user),
):
    patient = get_patient_by_id(db, patient_id)

    if not patient:
        raise HTTPException(status_code=404, detail="Patient not found")

    return patient


# 🔐 List All Patients (Any Logged-In User)
@router.get("/", response_model=List[PatientResponse])
def list_patients(
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user),
):
    return get_all_patients(db)
