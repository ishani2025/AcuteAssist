from sqlalchemy.orm import Session
from database.models import Hospital


def create_hospital(db: Session, data: dict):
    hospital = Hospital(**data)
    db.add(hospital)
    db.commit()
    db.refresh(hospital)
    return hospital


def get_all_hospitals(db: Session):
    return db.query(Hospital).all()
