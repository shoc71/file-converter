from docx import Document

class TextConverter:

    def txt_to_docx(self, input_path, output_path):
        doc = Document()
        with open(input_path) as f:
            for line in f:
                doc.add_paragraph(line.strip())

        doc.save(output_path)
        return output_path