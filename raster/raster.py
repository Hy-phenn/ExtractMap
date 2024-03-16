from raster.create_raster import create_raster
from raster.extract import get_cropped_map
from raster.boundaries import get_coordinates
from raster.get_geojson import geojson
from raster.view import view

def georeferenced_raster(city, image_path, show=False):

    geojson_path = geojson(city)

    cropped_map = get_cropped_map(image_path, True)
    coordinates = get_coordinates(geojson_path)
    raster = create_raster(coordinates, cropped_map)

    if show:
        view(raster)

    return raster


