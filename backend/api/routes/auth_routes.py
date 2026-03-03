from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database.db import get_db
from database.user_repository import create_user
from models.schemas import UserCreate, UserResponse,UserLogin
import hashlib
from passlib.context import CryptContext

from auth.jwt_handler import create_access_token
from database.user_repository import get_user_by_email
from fastapi import HTTPException
router = APIRouter(prefix="/auth", tags=["Auth"])
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

@router.post("/register", response_model=UserResponse)
def register_user(user: UserCreate, db: Session = Depends(get_db)):

    print("➡️ Register endpoint hit")

    existing_user = get_user_by_email(db, user.email)
    print("➡️ Checked existing user")

    if existing_user:
        print("❌ Email already exists")
        raise HTTPException(status_code=400, detail="Email already registered")

    print("➡️ Hashing password")
    hashed_password = pwd_context.hash(user.password)

    print("➡️ Creating user in DB")
    new_user = create_user(
        db,
        name=user.name,
        email=user.email,
        hashed_password=hashed_password,
        role=user.role
    )

    print("✅ User created successfully")
    return new_user
from fastapi.security import OAuth2PasswordRequestForm

@router.post("/login")
def login_user(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):
    db_user = get_user_by_email(db, form_data.username)

    if not db_user:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    if not pwd_context.verify(form_data.password, db_user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    access_token = create_access_token(
        data={"sub": db_user.email, "role": db_user.role}
    )

    return {"access_token": access_token, "token_type": "bearer"}
