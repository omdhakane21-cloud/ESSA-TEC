from fastapi import APIRouter, Depends, HTTPException, UploadFile, File
from sqlalchemy.orm import Session
from typing import List
from ..config.database import get_db
from ..models.event import Event
from ..schemas.event import EventCreate, EventUpdate, EventResponse
from ..middleware.auth import get_current_admin
from ..utils.file_upload import save_upload_file

router = APIRouter(prefix="/events", tags=["Events"])

@router.get("/", response_model=List[EventResponse])
def get_events(db: Session = Depends(get_db)):
    return db.query(Event).order_by(Event.id.desc()).all()

@router.post("/", response_model=EventResponse)
def create_event(event: EventCreate, db: Session = Depends(get_db), current_admin = Depends(get_current_admin)):
    db_event = Event(**event.model_dump())
    db.add(db_event)
    db.commit()
    db.refresh(db_event)
    return db_event

@router.put("/{event_id}", response_model=EventResponse)
def update_event(event_id: int, event_update: EventUpdate, db: Session = Depends(get_db), current_admin = Depends(get_current_admin)):
    db_event = db.query(Event).filter(Event.id == event_id).first()
    if not db_event:
        raise HTTPException(status_code=404, detail="Event not found")
    for key, value in event_update.model_dump(exclude_unset=True).items():
        setattr(db_event, key, value)
    db.commit()
    db.refresh(db_event)
    return db_event

@router.delete("/{event_id}")
def delete_event(event_id: int, db: Session = Depends(get_db), current_admin = Depends(get_current_admin)):
    db_event = db.query(Event).filter(Event.id == event_id).first()
    if not db_event:
        raise HTTPException(status_code=404, detail="Event not found")
    db.delete(db_event)
    db.commit()
    return {"message": "Event deleted successfully"}

@router.post("/upload")
def upload_event_image(file: UploadFile = File(...), current_admin = Depends(get_current_admin)):
    file_path = save_upload_file(file, "uploads/events")
    return {"url": file_path}
