import geopandas as gpd
import matplotlib.pyplot as plt
import requests

CITY = "GOURFALEUR"

def geojson(city):
    osm_id = get_id(city)
    if osm_id:
        return get_geojson(osm_id)

def show_polygon(geojson_file):
    gdf = gpd.read_file(geojson_file)
    gdf.plot()
    plt.show()

def get_geojson(osm_id):
    get_geojson_url = f"https://polygons.openstreetmap.fr/get_geojson.py?id={osm_id}&params=0"
    response = requests.get(get_geojson_url)

    if response.status_code == requests.codes.ok:
        with open(r'raster/temp/response.geojson', 'wb') as f:
            f.write(response.content)
        print("GeoJSON file saved successfully")
        return r'raster/temp/response.geojson'
    print("error getting GeoJSON")
    return False


def get_id(city):
    get_id_url = f"https://nominatim.openstreetmap.org/search.php?q={city}&format=jsonv2"
    response = requests.get(get_id_url)

    if response.status_code == requests.codes.ok:
        data = response.json()
        if len(data) > 0:
            osm_id = data[0]['osm_id']
            print("Id retrieved successfully", osm_id)
            return osm_id
    
    print("error getting Id")
    return False

if __name__ == "__main__":
    osm_id = get_id(CITY)
    if osm_id:
        geojson_file = get_geojson(osm_id)
    if geojson_file:
        show_polygon(geojson_file)

