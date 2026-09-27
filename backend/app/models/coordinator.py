from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from ..config.database import Base

class Coordinator(Base):
    __tablename__ = "coordinators"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(150), nullable=False)
    role = Column(String(150), nullable=False)
    phone = Column(String(50), nullable=False)
    email = Column(String(150), nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
