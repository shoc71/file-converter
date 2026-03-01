import os
from .strategies.pdf import PDFConverter
from .strategies.image import ImageConverter
from .strategies.text import TextConverter

class ConversionService:

    def __init__(self):
        self.pdf = PDFConverter()
        self.image = ImageConverter()
        self.text = TextConverter()

    def convert(self, input_path: str, action: str):
        name, _ = os.path.splitext(input_path)

        if action == "pdf-to-text":
            return self.pdf.pdf_to_text(input_path, name + ".txt")

        if action == "jpg-to-png":
            return self.image.jpg_to_png(input_path, name + ".png")

        if action == "txt-to-docx":
            return self.text.txt_to_docx(input_path, name + ".docx")

        raise ValueError("Unsupported conversion")