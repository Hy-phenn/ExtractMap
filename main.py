import os
from raster.raster import georeferenced_raster
from classify.predict import is_map
from classify.convert import Pdf

pdfs = os.listdir("pdfs")
pdf_name = pdfs[0]
city = pdf_name[:-4]
pdf_path = "pdfs/" + pdf_name

pdf = Pdf(pdf_path)

image_path = pdf.next_page()

while image_path:
    if is_map(image_path):
        raster_path = georeferenced_raster(city, image_path, show=True)
        break
    image_path = pdf.next_page()
