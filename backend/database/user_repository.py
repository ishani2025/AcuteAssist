from sqlalchemy.orm import Session
from database.models import User
import uuid


def create_user(db: Session, name: str, email: str, hashed_password: str, role: str):
    user = User(
        id=str(uuid.uuid4()),
        name=name,
        email=email,
        hashed_password=hashed_password,
        role=role
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()
