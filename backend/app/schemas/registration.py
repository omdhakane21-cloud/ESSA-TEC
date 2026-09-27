from pydantic import BaseModel, EmailStr
from datetime import datetime

class RegistrationCreate(BaseModel):
    event_id: int
    event_title: str
    student_name: str
    email: EmailStr
    phone: str
    year: str
    roll_no: str

class RegistrationResponse(RegistrationCreate):
    id: int
    status: str
    registered_at: datetime

    class Config:
        from_attributes = True
