from pydantic import BaseModel
from datetime import date, datetime
from typing import Optional


class PatientCreate(BaseModel):
    aadhaar_hash: str
    full_name: str
    dob: date
    gender: str
    mobile_number: Optional[str] = None


class PatientResponse(BaseModel):
    id: str
    aadhaar_hash: str
    full_name: str
    dob: date
    gender: str
    mobile_number: Optional[str] = None
    created_at: datetime

class HospitalCreate(BaseModel):
    hospital_name: str
    location: str


class HospitalResponse(BaseModel):
    id: str
    hospital_name: str
    location: str
    created_at: datetime
class PatientHospitalLinkCreate(BaseModel):
    patient_id: str
    hospital_id: str

class UserCreate(BaseModel):
    name: str
    email: str
    password: str
    role: str  # doctor, nurse, receptionist

class UserLogin(BaseModel):
    email: str
    password: str
    
class UserResponse(BaseModel):
    id: str
    name: str
    email: str
    role: str
from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class MedicalTestCreate(BaseModel):
    patient_id: str
    hospital_id: Optional[str] = None
    test_type: str
    value: float
    unit: Optional[str] = None
    reference_range: Optional[str] = None
    is_abnormal: bool
    test_date: datetime

class MedicalTestResponse(MedicalTestCreate):
    id: str
    created_at: datetime

    class Config:
        orm_mode = True
    class Config:
        from_attributes = True   
    class Config:
        from_attributes = True
    class Config:
       from_attributes = True
