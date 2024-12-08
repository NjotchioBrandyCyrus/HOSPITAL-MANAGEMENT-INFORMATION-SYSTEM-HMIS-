from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models import User

router = APIRouter()

@router.get("/")
def get_doctors(db: Session = Depends(SessionLocal)):
    doctors = db.query(User).filter(User.role == "doctor").all()
    return doctors

@router.post("/")
def create_doctor(name: str, email: str, password: str, db: Session = Depends(SessionLocal)):
    hashed_password = get_password_hash(password)
    doctor = User(name=name, email=email, hashed_password=hashed_password, role="doctor")
    db.add(doctor)
    db.commit()
    db.refresh(doctor)
    return doctor
