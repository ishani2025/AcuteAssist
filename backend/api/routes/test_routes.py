from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database.db import get_db
from database.models import MedicalTest
from models.schemas import MedicalTestCreate, MedicalTestResponse
import uuid
from datetime import datetime

router = APIRouter(prefix="/medical-tests", tags=["Medical Tests"])

@router.post("/", response_model=MedicalTestResponse)
def create_medical_test(test: MedicalTestCreate, db: Session = Depends(get_db)):

    new_test = MedicalTest(
        id=str(uuid.uuid4()),
        patient_id=test.patient_id,
        hospital_id=test.hospital_id,
        test_type=test.test_type,
        value=test.value,
        unit=test.unit,
        reference_range=test.reference_range,
        is_abnormal=test.is_abnormal,
        test_date=test.test_date,
        created_at=datetime.utcnow()
    )

    db.add(new_test)
    db.commit()
    db.refresh(new_test)

    return new_test
