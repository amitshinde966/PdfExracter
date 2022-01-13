import fitz
import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# read pdf file
pdf = fitz.open('eXuler.pdf')
# iterate through pdf pages
for page in range(0, len(pdf)):
    # load pages with index
    pages = pdf.loadPage(page)
    # take image of page
    img = pages.getPixmap()
    # save image
    img.writeImage(f'image{page + 1}.png')
    openImg = Image.open(f'image{page + 1}.png')
    text = pytesseract.image_to_string(openImg)
    print(text)