from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models import Patient
from app.schemas import PatientCreate

router = APIRouter()

@router.get("/")
def get_patients(db: Session = Depends(SessionLocal)):
    patients = db.query(Patient).all()
    return patients

@router.post("/")
def create_patient(patient: PatientCreate, db: Session = Depends(SessionLocal)):
    db_patient = Patient(**patient.dict())
    db.add(db_patient)
    db.commit()
    db.refresh(db_patient)
    return db_patient
