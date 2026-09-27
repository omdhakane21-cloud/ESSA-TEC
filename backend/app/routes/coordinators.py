from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from ..config.database import get_db
from ..models.coordinator import Coordinator
from ..schemas.coordinator import CoordinatorCreate, CoordinatorUpdate, CoordinatorResponse
from ..middleware.auth import get_current_admin

router = APIRouter(prefix="/coordinators", tags=["Coordinators"])

@router.get("/", response_model=List[CoordinatorResponse])
def get_coordinators(db: Session = Depends(get_db)):
    return db.query(Coordinator).all()

@router.post("/", response_model=CoordinatorResponse)
def add_coordinator(coord: CoordinatorCreate, db: Session = Depends(get_db), current_admin = Depends(get_current_admin)):
    db_coord = Coordinator(**coord.model_dump())
    db.add(db_coord)
    db.commit()
    db.refresh(db_coord)
    return db_coord

@router.put("/{coord_id}", response_model=CoordinatorResponse)
def update_coordinator(coord_id: int, update_data: CoordinatorUpdate, db: Session = Depends(get_db), current_admin = Depends(get_current_admin)):
    coord = db.query(Coordinator).filter(Coordinator.id == coord_id).first()
    if not coord:
        raise HTTPException(status_code=404, detail="Coordinator not found")
    for key, value in update_data.model_dump(exclude_unset=True).items():
        setattr(coord, key, value)
    db.commit()
    db.refresh(coord)
    return coord

@router.delete("/{coord_id}")
def delete_coordinator(coord_id: int, db: Session = Depends(get_db), current_admin = Depends(get_current_admin)):
    coord = db.query(Coordinator).filter(Coordinator.id == coord_id).first()
    if not coord:
        raise HTTPException(status_code=404, detail="Coordinator not found")
    db.delete(coord)
    db.commit()
    return {"message": "Coordinator deleted"}
