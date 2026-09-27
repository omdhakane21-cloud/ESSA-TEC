from sqlalchemy import Column, Integer, String, Text, DateTime
from datetime import datetime
from ..config.database import Base

class TeamMember(Base):
    __tablename__ = "team_members"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(150), nullable=False)
    role = Column(String(150), nullable=False)
    category = Column(String(50), default="mentor")  # mentor, core, committee
    image_url = Column(String(500), nullable=True)
    department = Column(String(100), default="Electronics Engineering")
    linkedin = Column(String(255), nullable=True)
    instagram = Column(String(255), nullable=True)
    bio = Column(Text, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
