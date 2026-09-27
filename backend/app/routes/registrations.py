from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from ..config.database import get_db
from ..models.registration import Registration
from ..schemas.registration import RegistrationCreate, RegistrationResponse
from ..middleware.auth import get_current_admin

router = APIRouter(prefix="/registrations", tags=["Registrations"])

@router.get("/", response_model=List[RegistrationResponse])
def get_registrations(db: Session = Depends(get_db), current_admin = Depends(get_current_admin)):
    return db.query(Registration).order_by(Registration.id.desc()).all()

@router.post("/", response_model=RegistrationResponse)
def register_event(reg: RegistrationCreate, db: Session = Depends(get_db)):
    db_reg = Registration(**reg.model_dump())
    db.add(db_reg)
    db.commit()
    db.refresh(db_reg)
    return db_reg

@router.delete("/{reg_id}")
def delete_registration(reg_id: int, db: Session = Depends(get_db), current_admin = Depends(get_current_admin)):
    reg = db.query(Registration).filter(Registration.id == reg_id).first()
    if not reg:
        raise HTTPException(status_code=404, detail="Registration not found")
    db.delete(reg)
    db.commit()
    return {"message": "Registration deleted"}
