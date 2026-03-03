from sqlalchemy.orm import Session
from database.models import MedicalTest

def get_tests_by_patient(db: Session, patient_id: str):
    return db.query(MedicalTest).filter(
        MedicalTest.patient_id == patient_id
    ).all()
