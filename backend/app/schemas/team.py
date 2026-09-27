from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class TeamBase(BaseModel):
    name: str
    role: str
    category: str = "mentor"
    image_url: Optional[str] = None
    department: Optional[str] = "Electronics Engineering"
    linkedin: Optional[str] = None
    instagram: Optional[str] = None
    bio: Optional[str] = None

class TeamCreate(TeamBase):
    pass

class TeamUpdate(BaseModel):
    name: Optional[str] = None
    role: Optional[str] = None
    category: Optional[str] = None
    image_url: Optional[str] = None
    department: Optional[str] = None
    linkedin: Optional[str] = None
    instagram: Optional[str] = None
    bio: Optional[str] = None

class TeamResponse(TeamBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True
