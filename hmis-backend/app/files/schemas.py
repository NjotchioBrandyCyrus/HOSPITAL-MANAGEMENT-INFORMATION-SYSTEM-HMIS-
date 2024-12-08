from pydantic import BaseModel

class UserBase(BaseModel):
    name: str
    email: str
    role: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int

    class Config:
        orm_mode = True

class PatientBase(BaseModel):
    address: str
    contact: str
    medical_history: str

class PatientCreate(PatientBase):
    pass

class Patient(PatientBase):
    id: int
    user_id: int

    class Config:
        orm_mode = True
