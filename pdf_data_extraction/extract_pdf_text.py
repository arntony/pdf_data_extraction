
import os
try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract


def ocr_core(filename):
    """
    This function will handle the core OCR processing of images.
    """
    text = pytesseract.image_to_string(Image.open(filename))  # We'll use Pillow's Image class to open the image and pytesseract to detect the string in the image
    return text


test = False
if test:
    filepath = r'C:\python_projects\pdf_data_extraction\pdf_data_extraction\pdf_images'
    filename = '00a7d8b0-5279-4b1d-82e8-122ad6d832e0-02.jpg'
    print(ocr_core(os.path.join(filepath, filename)))
