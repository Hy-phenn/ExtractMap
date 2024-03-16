import json
import numpy as np

def get_coordinates(file_path):
    with open(file_path, "r") as file:
        data = json.load(file)
        coordinates = data["coordinates"][0][0]

    coordinates_array = np.array(coordinates)

    leftmost_x = float('inf')  
    top_y = float('inf')
    rightmost_x = -float('inf')
    bottom_y = -float('inf')

    for point in coordinates_array:
        x, y = point
            
        if x < leftmost_x:
            leftmost_x = x
        
        if x > rightmost_x:
            rightmost_x = x
        
        if y < top_y:
            top_y = y
        
        if y > bottom_y:
            bottom_y = y

    print("Got coordinates successfully")
        
    return [leftmost_x, top_y, rightmost_x, bottom_y]

if __name__ == '__main__':
    print(get_coordinates('response.geojson'))