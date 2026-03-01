import fitz

class PDFConverter:

    def pdf_to_text(self, input_path, output_path):
        doc = fitz.open(input_path)
        text = ""

        for page in doc:
            text += page.get_text()

        with open(output_path, "w", encoding="utf-8") as f:
            f.write(text)

        return output_path