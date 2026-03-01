# Service Layer - (Business Logic)

from pathlib import Path
from fastapi import UploadFile
from app.services.file_service import FileService
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from server.app.services.base import BaseService

class ConversionService(BaseService):

    def __init__(self):
        self.file_service = FileService()

    async def txt_to_pdf(self, file: UploadFile) -> Path:
        input_path = await self.file_service.save_upload(file)
        output_path = input_path.with_suffix(".pdf")

        doc = SimpleDocTemplate(str(output_path))
        styles = getSampleStyleSheet()

        elements = []

        with open(input_path, encoding="utf-8") as f:
            for line in f:
                elements.append(Paragraph(line, styles["Normal"]))

        doc.build(elements)

        return output_path