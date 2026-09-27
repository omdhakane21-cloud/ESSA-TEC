from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class EventBase(BaseModel):
    title: str
    category: str = "Technical"
    date_str: str
    time_str: Optional[str] = None
    venue: str
    description: str
    image_url: Optional[str] = None
    status: str = "upcoming"
    is_active: bool = True

class EventCreate(EventBase):
    pass

class EventUpdate(BaseModel):
    title: Optional[str] = None
    category: Optional[str] = None
    date_str: Optional[str] = None
    time_str: Optional[str] = None
    venue: Optional[str] = None
    description: Optional[str] = None
    image_url: Optional[str] = None
    status: Optional[str] = None
    is_active: Optional[bool] = None

class EventResponse(EventBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True
