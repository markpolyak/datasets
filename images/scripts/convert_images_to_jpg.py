import os
from PIL import Image

EXTENSIONS = (".JPG", ".jpeg", ".bmp", ".gif", ".HEIC")
root_directory ="dumpsters"
DESTINATIONAL_EXTENSION = ".jpg"

def convert_to_jpeg(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(EXTENSIONS):
                file_path = os.path.join(root, file)
                image = Image.open(file_path).convert('RGB')
                image.save(os.path.splitext(file_path)[0] + DESTINATIONAL_EXTENSION, "JPEG")
                os.remove(file_path)
                print(f"Converted {file} to {DESTINATIONAL_EXTENSION}")

# Укажите путь к корневой папке, в которой нужно обработать изображения


convert_to_jpeg(root_directory)