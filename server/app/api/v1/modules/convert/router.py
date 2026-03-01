from fastapi import APIRouter, UploadFile, Depends
from fastapi.responses import FileResponse

from app.shared.dependencies import get_storage
from app.shared.file_utils import unique_filename
from .service import ConversionService

router = APIRouter()
service = ConversionService()

@router.post("/{action}")
def convert_file(action: str, file: UploadFile, storage=Depends(get_storage)):
    filename = unique_filename(file.filename)

    input_path = storage.save(file, filename)

    output_path = service.convert(input_path, action)

    return FileResponse(output_path, filename=output_path.split("/")[-1])