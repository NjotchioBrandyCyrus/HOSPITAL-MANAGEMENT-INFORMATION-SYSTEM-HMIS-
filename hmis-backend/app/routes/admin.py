from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models import User
from app.schemas import UserCreate
from app.crud import create_user, get_password_hash

router = APIRouter()


@router.get("/")
def get_admins(db: Session = Depends(SessionLocal)):
    """Retrieve all admins."""
    admins = db.query(User).filter(User.role == "admin").all()
    return admins


@router.post("/")
def create_admin(user: UserCreate, db: Session = Depends(SessionLocal)):
    """Create a new admin account."""
    existing_user = db.query(User).filter(User.email == user.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    hashed_password = get_password_hash(user.password)
    admin_user = User(
        name=user.name,
        email=user.email,
        hashed_password=hashed_password,
        role="admin"
    )
    db.add(admin_user)
    db.commit()
    db.refresh(admin_user)
    return admin_user


@router.delete("/{admin_id}")
def delete_admin(admin_id: int, db: Session = Depends(SessionLocal)):
    """Delete an admin by ID."""
    admin = db.query(User).filter(User.id == admin_id, User.role == "admin").first()
    if not admin:
        raise HTTPException(status_code=404, detail="Admin not found")
    db.delete(admin)
    db.commit()
    return {"message": "Admin deleted successfully"}
