from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from ..config.database import Base

class GalleryItem(Base):
    __tablename__ = "gallery"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(200), nullable=False)
    category = Column(String(100), default="Workshops")
    image_url = Column(String(500), nullable=False)
    description = Column(String(500), nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
