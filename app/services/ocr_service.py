import pytesseract
from PIL import Image

# Tesseract installation path
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


def extract_text_from_image(image_file):

    image = Image.open(image_file)

    text = pytesseract.image_to_string(
        image,
        lang="eng+hin+guj"
    )

    return text.strip()