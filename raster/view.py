import rasterio
from rasterio.plot import show
def view(fp):
    img = rasterio.open(fp)
    show(img)