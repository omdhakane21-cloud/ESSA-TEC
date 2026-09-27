from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from ..config.database import get_db
from ..models.message import Message
from ..schemas.message import MessageCreate, MessageResponse
from ..middleware.auth import get_current_admin

router = APIRouter(prefix="/messages", tags=["Messages"])

@router.get("/", response_model=List[MessageResponse])
def get_messages(db: Session = Depends(get_db), current_admin = Depends(get_current_admin)):
    return db.query(Message).order_by(Message.id.desc()).all()

@router.post("/", response_model=MessageResponse)
def send_message(msg: MessageCreate, db: Session = Depends(get_db)):
    db_msg = Message(**msg.model_dump())
    db.add(db_msg)
    db.commit()
    db.refresh(db_msg)
    return db_msg

@router.put("/{msg_id}/toggle-read")
def toggle_read(msg_id: int, db: Session = Depends(get_db), current_admin = Depends(get_current_admin)):
    msg = db.query(Message).filter(Message.id == msg_id).first()
    if not msg:
        raise HTTPException(status_code=404, detail="Message not found")
    msg.is_read = not msg.is_read
    db.commit()
    return {"status": "success", "is_read": msg.is_read}

@router.delete("/{msg_id}")
def delete_message(msg_id: int, db: Session = Depends(get_db), current_admin = Depends(get_current_admin)):
    msg = db.query(Message).filter(Message.id == msg_id).first()
    if not msg:
        raise HTTPException(status_code=404, detail="Message not found")
    db.delete(msg)
    db.commit()
    return {"message": "Message deleted"}
