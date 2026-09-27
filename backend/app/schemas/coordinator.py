from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class CoordinatorBase(BaseModel):
    name: str
    role: str
    phone: str
    email: Optional[str] = None

class CoordinatorCreate(CoordinatorBase):
    pass

class CoordinatorUpdate(BaseModel):
    name: Optional[str] = None
    role: Optional[str] = None
    phone: Optional[str] = None
    email: Optional[str] = None

class CoordinatorResponse(CoordinatorBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True
