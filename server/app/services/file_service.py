# File Service (Reusable File Logic)

from pathlib import Path
from fastapi import UploadFile
import shutil

UPLOAD_DIR = Path("uploads")
UPLOAD_DIR.mkdir(exist_ok=True)

class FileService:

    async def save_uploads(self, file: UploadFile) -> Path:
        path = UPLOAD_DIR / file.filename

        with open(path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        return path