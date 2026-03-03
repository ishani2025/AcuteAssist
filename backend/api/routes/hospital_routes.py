from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database.patient_hospital_repository import link_patient_to_hospital
from models.schemas import PatientHospitalLinkCreate
from database.db import get_db
from sqlalchemy.orm import Session
from fastapi import Depends
from database.db import get_db
from auth.role_checker import require_role
from database.hospital_repository import (
    create_hospital,
    get_all_hospitals,
)

from models.schemas import HospitalCreate, HospitalResponse

router = APIRouter(prefix="/hospitals", tags=["Hospitals"])



@router.post("/", response_model=HospitalResponse)
def register_hospital(
    hospital: HospitalCreate,
    db: Session = Depends(get_db),
    current_user = Depends(require_role("admin"))
):
    return create_hospital(db, hospital.dict())

@router.get("/", response_model=list[HospitalResponse])
def list_hospitals(db: Session = Depends(get_db)):
    return get_all_hospitals(db)

@router.post("/link/")
def link_patient(data: PatientHospitalLinkCreate, db: Session = Depends(get_db)):
    return link_patient_to_hospital(
        db,
        data.patient_id,
        data.hospital_id
    )
