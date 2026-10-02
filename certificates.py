from fastapi import APIRouter, HTTPException
from fastapi.responses import FileResponse
import os
from utils.certificate_gen import generate_certificate

router = APIRouter(prefix="/certificates", tags=["Certificates"])

@router.get("/download/{workshop_id}/{student_id}")
def download_certificate(workshop_id: int, student_id: int):
    # In production, fetch student name and workshop details from database here based on student_id & workshop_id
    student_name = "Alex Johnson" 
    workshop_name = "Multi-layer PCB Design & High-Speed Signal Integrity"
    date_str = "September 2026"

    os.makedirs("generated_certs", exist_ok=True)
    file_path = f"generated_certs/cert_{student_id}_{workshop_id}.pdf"
    
    generate_certificate(student_name, workshop_name, date_str, file_path)
    
    if os.path.exists(file_path):
        return FileResponse(file_path, media_type='application/pdf', filename=f"{student_name}_Certificate.pdf")
    
    raise HTTPException(status_code=500, detail="Error generating certificate")
