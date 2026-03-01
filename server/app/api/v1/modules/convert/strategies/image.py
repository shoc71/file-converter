from PIL import Image

class ImageConverter:

    def jpg_to_png(self, input_path, output_path):
        img = Image.open(input_path)
        img.save(output_path, "PNG")
        return output_path