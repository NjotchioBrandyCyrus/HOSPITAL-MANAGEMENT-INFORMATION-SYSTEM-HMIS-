from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas import UserCreate, Token
from app.crud import create_user, authenticate_user
from app.database import SessionLocal

router = APIRouter()

@router.post("/signup", response_model=Token)
def signup(user: UserCreate, db: Session = Depends(SessionLocal)):
    user = create_user(db, user)
    return {"access_token": user.email, "token_type": "bearer"}

@router.post("/login", response_model=Token)
def login(email: str, password: str, db: Session = Depends(SessionLocal)):
    user = authenticate_user(db, email, password)
    if not user:
        raise HTTPException(status_code=400, detail="Invalid credentials")
    return {"access_token": user.email, "token_type": "bearer"}
