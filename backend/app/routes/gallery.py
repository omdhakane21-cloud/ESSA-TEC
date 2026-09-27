from fastapi import APIRouter, Depends, HTTPException, UploadFile, File
from sqlalchemy.orm import Session
from typing import List
from ..config.database import get_db
from ..models.gallery import GalleryItem
from ..schemas.gallery import GalleryCreate, GalleryResponse
from ..middleware.auth import get_current_admin
from ..utils.file_upload import save_upload_file

router = APIRouter(prefix="/gallery", tags=["Gallery"])

@router.get("/", response_model=List[GalleryResponse])
def get_gallery(db: Session = Depends(get_db)):
    return db.query(GalleryItem).order_by(GalleryItem.id.desc()).all()

@router.post("/", response_model=GalleryResponse)
def add_gallery_item(item: GalleryCreate, db: Session = Depends(get_db), current_admin = Depends(get_current_admin)):
    db_item = GalleryItem(**item.model_dump())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

@router.delete("/{item_id}")
def delete_gallery_item(item_id: int, db: Session = Depends(get_db), current_admin = Depends(get_current_admin)):
    db_item = db.query(GalleryItem).filter(GalleryItem.id == item_id).first()
    if not db_item:
        raise HTTPException(status_code=404, detail="Item not found")
    db.delete(db_item)
    db.commit()
    return {"message": "Photo deleted"}

@router.post("/upload")
def upload_gallery_photo(file: UploadFile = File(...), current_admin = Depends(get_current_admin)):
    file_path = save_upload_file(file, "uploads/gallery")
    return {"url": file_path}
