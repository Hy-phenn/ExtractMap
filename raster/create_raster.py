from osgeo import gdal

def create_raster(coordinates, image_path):

    output_raster = "output.tif"

    ds = gdal.Open(image_path)

    gt = gdal.Translate('output.tif', ds,
                    outputBounds = coordinates,
                    outputSRS="EPSG:4326"
                    )

    print("Raster created successfully")

    print("Raster saved at", output_raster)

    return output_raster
