import cv2
import numpy as np

THRESHOLD1 = 175
THRESHOLD2 = 0

MIN_AREA = 10000

IMAGE_PATH = r"image9_1.png"

def get_cropped_map(img_path, show_img=False):
    image = cv2.imread(img_path)

    imgCountour = image.copy()
    imgBlur = cv2.GaussianBlur(image, (7, 7), 1)

    imgCanny = cv2.Canny(imgBlur, THRESHOLD1, THRESHOLD2)
    kernel = np.ones((5, 5))
    imgDil = cv2.dilate(imgCanny, kernel, iterations=1)

    contours, _ = cv2.findContours(imgDil, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    contour = None

    max_area = 0
    for cnt in contours:
        if cv2.contourArea(cnt) > max_area:
            contour = cnt

    print("Found contour of map successfully")

    x, y, w, h = cv2.boundingRect(contour)

    cropped_img = image[y:y+h, x:x+w]

    cropped_img_path = r"raster/temp/map_extracted.png"

    cv2.imwrite(cropped_img_path, cropped_img)

    print("Map cropped successfully")

    
    if show_img:
        cv2.drawContours(imgCountour, contour, -1, (255, 0, 7), 7) #visual
        
        cv2.namedWindow("Image", cv2.WINDOW_NORMAL) #visual
        cv2.resizeWindow("Image", 1000, 1000) #visual
        cv2.imshow("Image", imgCountour) #visual
        cv2.waitKey(20000) #visual

    
    return cropped_img_path

if __name__ == '__main__':
    get_cropped_map(IMAGE_PATH, True)
    
        