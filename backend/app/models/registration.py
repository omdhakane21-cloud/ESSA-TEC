from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from datetime import datetime
from ..config.database import Base

class Registration(Base):
    __tablename__ = "registrations"

    id = Column(Integer, primary_key=True, index=True)
    event_id = Column(Integer, nullable=False)
    event_title = Column(String(200), nullable=False)
    student_name = Column(String(150), nullable=False)
    email = Column(String(150), nullable=False)
    phone = Column(String(20), nullable=False)
    year = Column(String(20), nullable=False)
    roll_no = Column(String(50), nullable=False)
    status = Column(String(50), default="Confirmed")
    registered_at = Column(DateTime, default=datetime.utcnow)
