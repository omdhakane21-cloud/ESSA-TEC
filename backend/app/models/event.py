from sqlalchemy import Column, Integer, String, Text, DateTime, Boolean
from datetime import datetime
from ..config.database import Base

class Event(Base):
    __tablename__ = "events"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(200), nullable=False)
    category = Column(String(100), default="Technical")
    date_str = Column(String(100), nullable=False)
    time_str = Column(String(100), nullable=True)
    venue = Column(String(200), nullable=False)
    description = Column(Text, nullable=False)
    image_url = Column(String(500), nullable=True)
    status = Column(String(50), default="upcoming")
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)
