import os
import shutil
import uuid
from fastapi import UploadFile

def save_upload_file(upload_file: UploadFile, folder: str = "uploads") -> str:
    os.makedirs(folder, exist_ok=True)
    extension = os.path.splitext(upload_file.filename)[1]
    unique_filename = f"{uuid.uuid4().hex}{extension}"
    file_path = os.path.join(folder, unique_filename)
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(upload_file.file, buffer)
    return f"/{file_path}"
