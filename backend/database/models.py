import uuid
from datetime import datetime
from sqlalchemy import Column, String, Date, DateTime, Boolean, ForeignKey, Float
from sqlalchemy.orm import relationship
from .db import Base


def generate_uuid():
    return str(uuid.uuid4())


class Patient(Base):
    __tablename__ = "patients"

    id = Column(String, primary_key=True, default=generate_uuid)
    aadhaar_hash = Column(String, unique=True, nullable=False)
    full_name = Column(String, nullable=False)
    dob = Column(Date, nullable=False)
    gender = Column(String, nullable=False)
    mobile_number = Column(String, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)


class Hospital(Base):
    __tablename__ = "hospitals"

    id = Column(String, primary_key=True, default=generate_uuid)
    hospital_name = Column(String, nullable=False)
    location = Column(String, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)


class PatientHospitalLink(Base):
    __tablename__ = "patient_hospital_links"

    id = Column(String, primary_key=True, default=generate_uuid)
    patient_id = Column(String, ForeignKey("patients.id"))
    hospital_id = Column(String, ForeignKey("hospitals.id"))
    linked_at = Column(DateTime, default=datetime.utcnow)


class MedicalTest(Base):
    __tablename__ = "medical_tests"

    id = Column(String, primary_key=True, default=generate_uuid)
    patient_id = Column(String, ForeignKey("patients.id"))
    hospital_id = Column(String, ForeignKey("hospitals.id"))
    test_type = Column(String, nullable=False)
    value = Column(Float, nullable=True)
    unit = Column(String, nullable=True)
    reference_range = Column(String, nullable=True)
    is_abnormal = Column(Boolean, default=False)
    test_date = Column(DateTime, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)


class AuditLog(Base):
    __tablename__ = "audit_logs"

    id = Column(String, primary_key=True, default=generate_uuid)
    user_role = Column(String, nullable=False)
    patient_id = Column(String, nullable=True)
    action_type = Column(String, nullable=False)
    timestamp = Column(DateTime, default=datetime.utcnow)

class User(Base):
    __tablename__ = "users"

    id = Column(String, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String, nullable=False)
    role = Column(String, nullable=False)  # doctor, nurse, receptionist
    created_at = Column(DateTime, default=datetime.utcnow)
