from fastapi import FastAPI
from app.routes import auth, patients, doctors, admin

app = FastAPI()

# Include routes
app.include_router(auth.router, prefix="/auth", tags=["Authentication"])
app.include_router(patients.router, prefix="/patients", tags=["Patients"])
app.include_router(doctors.router, prefix="/doctors", tags=["Doctors"])
app.include_router(admin.router, prefix="/admin", tags=["Admin"])

@app.get("/")
def root():
    return {"message": "Welcome to HMIS API"}
