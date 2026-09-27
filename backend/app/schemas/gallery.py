from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class GalleryBase(BaseModel):
    title: str
    category: str = "Workshops"
    image_url: str
    description: Optional[str] = None

class GalleryCreate(GalleryBase):
    pass

class GalleryResponse(GalleryBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True
