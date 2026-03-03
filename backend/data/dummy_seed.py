import random
from datetime import datetime, timedelta
from sqlalchemy.orm import Session

from database.db import SessionLocal
from database.models import Patient, MedicalTest
import uuid


def seed_dummy_data():

    db: Session = SessionLocal()

    print("Seeding dummy data...")

    for i in range(50):

        patient_id = str(uuid.uuid4())

        patient = Patient(
            id=patient_id,
            aadhaar_hash=f"HASH_{i}",
            full_name=f"Patient_{i}",
            dob=datetime(1990, 1, 1),
            gender=random.choice(["Male", "Female"]),
            mobile_number=f"90000000{i}"
        )

        db.add(patient)

        # Random troponin
        troponin_value = round(random.uniform(0.01, 1.2), 2)

        troponin_test = MedicalTest(
            id=str(uuid.uuid4()),
            patient_id=patient_id,
            hospital_id=None,
            test_type="troponin",
            value=troponin_value,
            unit="ng/mL",
            reference_range="0.0 - 0.4",
            is_abnormal=troponin_value > 0.4,
            test_date=datetime.utcnow()
        )

        # Random blood pressure
        bp_value = random.randint(100, 200)

        bp_test = MedicalTest(
            id=str(uuid.uuid4()),
            patient_id=patient_id,
            hospital_id=None,
            test_type="blood_pressure",
            value=bp_value,
            unit="mmHg",
            reference_range="90 - 140",
            is_abnormal=bp_value > 180,
            test_date=datetime.utcnow()
        )

        db.add(troponin_test)
        db.add(bp_test)

    db.commit()
    db.close()

    print("Dummy data inserted successfully!")


if __name__ == "__main__":
    seed_dummy_data()
