from sqlalchemy.orm import Session
from database.models import Patient
import uuid


def create_patient(db: Session, patient_data):

    new_patient = Patient(
        id=str(uuid.uuid4()),
        aadhaar_hash=patient_data["aadhaar_hash"],
        full_name=patient_data["full_name"],
        dob=patient_data["dob"],
        gender=patient_data["gender"],
        mobile_number=patient_data["mobile_number"]
    )

    db.add(new_patient)
    db.commit()
    db.refresh(new_patient)

    return new_patient


def get_patient_by_id(db: Session, patient_id: str):
    return db.query(Patient).filter(Patient.id == patient_id).first()


def get_all_patients(db: Session):
    return db.query(Patient).all()
