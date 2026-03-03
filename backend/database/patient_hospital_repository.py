from sqlalchemy.orm import Session
from database.models import PatientHospitalLink


def link_patient_to_hospital(db: Session, patient_id: str, hospital_id: str):
    link = PatientHospitalLink(
        patient_id=patient_id,
        hospital_id=hospital_id
    )
    db.add(link)
    db.commit()
    db.refresh(link)
    return link


def get_hospitals_for_patient(db: Session, patient_id: str):
    return db.query(PatientHospitalLink).filter(
        PatientHospitalLink.patient_id == patient_id
    ).all()


def get_patients_for_hospital(db: Session, hospital_id: str):
    return db.query(PatientHospitalLink).filter(
        PatientHospitalLink.hospital_id == hospital_id
    ).all()
