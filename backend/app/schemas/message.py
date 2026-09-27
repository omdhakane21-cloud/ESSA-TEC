from pydantic import BaseModel, EmailStr
from datetime import datetime

class MessageCreate(BaseModel):
    name: str
    email: EmailStr
    subject: str
    message: str

class MessageResponse(MessageCreate):
    id: int
    is_read: bool
    created_at: datetime

    class Config:
        from_attributes = True
