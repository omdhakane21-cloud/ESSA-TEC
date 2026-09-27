from fastapi import APIRouter, Depends, HTTPException, UploadFile, File
from sqlalchemy.orm import Session
from typing import List
from ..config.database import get_db
from ..models.team import TeamMember
from ..schemas.team import TeamCreate, TeamUpdate, TeamResponse
from ..middleware.auth import get_current_admin
from ..utils.file_upload import save_upload_file

router = APIRouter(prefix="/team", tags=["Team"])

@router.get("/", response_model=List[TeamResponse])
def get_team(db: Session = Depends(get_db)):
    return db.query(TeamMember).all()

@router.post("/", response_model=TeamResponse)
def create_team_member(member: TeamCreate, db: Session = Depends(get_db), current_admin = Depends(get_current_admin)):
    db_member = TeamMember(**member.model_dump())
    db.add(db_member)
    db.commit()
    db.refresh(db_member)
    return db_member

@router.put("/{member_id}", response_model=TeamResponse)
def update_team_member(member_id: int, member_update: TeamUpdate, db: Session = Depends(get_db), current_admin = Depends(get_current_admin)):
    db_member = db.query(TeamMember).filter(TeamMember.id == member_id).first()
    if not db_member:
        raise HTTPException(status_code=404, detail="Member not found")
    for key, value in member_update.model_dump(exclude_unset=True).items():
        setattr(db_member, key, value)
    db.commit()
    db.refresh(db_member)
    return db_member

@router.delete("/{member_id}")
def delete_team_member(member_id: int, db: Session = Depends(get_db), current_admin = Depends(get_current_admin)):
    db_member = db.query(TeamMember).filter(TeamMember.id == member_id).first()
    if not db_member:
        raise HTTPException(status_code=404, detail="Member not found")
    db.delete(db_member)
    db.commit()
    return {"message": "Team member deleted"}

@router.post("/upload")
def upload_team_photo(file: UploadFile = File(...), current_admin = Depends(get_current_admin)):
    file_path = save_upload_file(file, "uploads/team")
    return {"url": file_path}
