import re

import pytesseract
from fastapi import FastAPI, File, UploadFile
from PIL import Image
import io
app = FastAPI()
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


@app.post("/ocr/")
async def ocr(file: UploadFile = File(...)):
    image = Image.open(io.BytesIO(await file.read()))
    text = pytesseract.image_to_string(image)
    clean_string = re.sub(r'[^\w\s]+', '', text.replace('\n', ' '))
    clean_string = re.sub(r'\s+', ' ', clean_string)
    # text = re.sub(r'(^[\W_\s]+|\s|\n|\\)', '', text)
    return {"text": clean_string}
