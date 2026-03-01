# Endpoint Layer - Thin Controllers

from fastapi import APIRouter, UploadFile, File
from fastapi.responses import FileResponse
from app.services.conversion_service import ConversionService

router = APIRouter(prefix="/convert", tags=["convert"])

@router.post("/txt-to-pdf")
async def txt_to_pdf(file: UploadFile = File(...)):
    service = ConversionService()
    output_path = await service.txt_to_pdf(file)
    return FileResponse(output_path)