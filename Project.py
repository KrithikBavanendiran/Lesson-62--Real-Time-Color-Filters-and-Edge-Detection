import cv2
import numpy as np

def apply_filter(image_path, filter_type):
    """Apply the selected color filter or edge detection."""
    filtered_image=image.copy()

    if filter_type == 'red_tint':
        filtered_image[:, :, 1] = 0
        filtered_image[:, :, 0] = 0
    elif filter_type == 'green_tint':
        filtered_image[:, :, 0] = 0
        filtered_image[:, :, 2] = 0
    elif filter_type == 'blue_tint':
        filtered_image[:, :, 1] = 0
        filtered_image[:, :, 2] = 0
    elif filter_type == 'yellow_tint':
        filtered_image[:, :, 0] = 0
        filtered_image[:, :, 2] = filtered_image[:, :, 2]
    elif filter_type == 'pink_tint':
        filtered_image[:, :, 0] = filtered_image[:, :, 0] // 2
        filtered_image[:, :, 1] = 0
        filtered_image[:, :, 2] = filtered_image[:, :, 2]
    elif filter_type == 'sobel':
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        sobelx = cv2.Sobel(gray_image, cv2.CV_64F, 1, 0, ksize=3)
        sobely = cv2.Sobel(gray_image, cv2.CV_64F, 0, 1, ksize=3)
        combined_sobel = cv2.bitwise_or(sobelx.astype('uint8'), sobely.astype('uint8'))
        filtered_image = cv2.cvtColor(combined_sobel, cv2.COLOR_GRAY2BGR)
    elif filter_type == 'canny':
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        edges = cv2.Canny(gray_image, 100, 200)
        filtered_image = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)
    elif filter_type == 'laplacian':
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        laplacian = cv2.Laplacian(gray_image, cv2.CV_64F)
        laplacian = cv2.convertScaleAbs(laplacian)
        filtered_image = cv2.cvtColor(laplacian, cv2.COLOR_GRAY2BGR)
    elif filter_type == 'guassian_blur':
        filtered_image = cv2.GaussianBlur(image, (15, 15), 0)
    elif filter_type == 'median_blur':
        filtered_image = cv2.medianBlur(image, 15)

    return filtered_image

image_path = 'example.jpg' 
image=cv2.imread(image_path)

if image is None:
    print("Error: Image not found.")
else:
    filter_type = 'original' 

    print("Press the following keys to apply filters:")
    print("r - Red Tint")
    print("g - Green Tint") 
    print("b - Blue Tint")
    print("y - Yellow Tint")
    print("p - Pink Tint")
    print("s - Sobel Edge Detection")
    print("c - Canny Edge Detection")
    print("l - Laplacian Edge Detection")
    print("f - Guassian Blur")
    print("m - Median Blur")
    print("q - Quit")

    while True:
        filtered_image = apply_filter(image_path, filter_type)

        cv2.imshow("Filtered Image", filtered_image)

        key= cv2.waitKey(0) & 0xFF

        if key == ord('r'):
            filter_type = 'red_tint'
        elif key == ord('g'):
            filter_type = 'green_tint'
        elif key == ord('b'):
            filter_type = 'blue_tint'
        elif key == ord('y'):
            filter_type = 'yellow_tint'
        elif key == ord('p'):
            filter_type = 'pink_tint'
        elif key == ord('s'):
            filter_type = 'sobel'
        elif key == ord('c'):
            filter_type = 'canny'
        elif key == ord('l'):
            filter_type = 'laplacian'
        elif key == ord('f'):
            filter_type = 'guassian_blur'
        elif key == ord('m'):
            filter_type = 'median_blur'
        elif key == ord('q'):
            break
        else:
            print("Invalid key! Please use 'r', 'g', 'b', 's', 'c', 'l', 'y', 'p', 'f', 'm', or 'q'.")
    
cv2.destroyAllWindows()