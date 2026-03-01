import uuid
from pathlib import Path

def unique_filename(filename: str) -> str:
    ext = Path(filename).suffix
    return f"{uuid.uuid4()}{ext}"