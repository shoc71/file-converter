from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from pathlib import Path
import shutil
import tempfile
from pdf2image import convert_from_path
from docx2pdf import convert as docx_to_pdf
from fpdf import FPDF

app = FastAPI()

# Allow your Angular frontend domain
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://file-converter-4sww.onrender.com/"],
    allow_methods=["*"],
    allow_headers=["*"],
)

UPLOAD_DIR = Path(tempfile.gettempdir()) / "uploads"
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)

@app.post("/convert/")
async def convert_file(file: UploadFile = File(...), target_format: str = "pdf"):
    input_path = UPLOAD_DIR / file.filename
    with input_path.open("wb") as f:
        shutil.copyfileobj(file.file, f)

    output_path = input_path.with_suffix(f".{target_format}")

    # Convert PDF -> Image
    if file.filename.lower().endswith(".pdf") and target_format.lower() in ["png", "jpg"]:
        images = convert_from_path(str(input_path))
        images[0].save(output_path, target_format.upper())

    # Convert DOCX -> PDF
    elif file.filename.lower().endswith(".docx") and target_format.lower() == "pdf":
        docx_to_pdf(str(input_path), str(output_path))

    # Convert TXT -> Image (simple example)
    elif file.filename.lower().endswith(".txt") and target_format.lower() in ["png", "jpg"]:
        with open(input_path) as f:
            text = f.read()
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        pdf.multi_cell(0, 5, txt=text)
        tmp_pdf = output_path.with_suffix(".pdf")
        pdf.output(tmp_pdf)
        images = convert_from_path(str(tmp_pdf))
        images[0].save(output_path, target_format.upper())
        tmp_pdf.unlink()  # remove intermediate

    else:
        # Fallback: return original file
        shutil.copy(str(input_path), str(output_path))

    return FileResponse(str(output_path), media_type="application/octet-stream", filename=output_path.name)
