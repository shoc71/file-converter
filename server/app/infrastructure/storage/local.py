import os
from app.core.config import settings

class LocalStorage:

    def save(self, file, filename: str) -> str:
        os.makedirs(settings.UPLOAD_DIR, exist_ok=True)
        path = os.path.join(settings.UPLOAD_DIR, filename)

        with open(path, "wb") as f:
            f.write(file.file.read())

        return path