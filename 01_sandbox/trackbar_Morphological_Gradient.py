import cv2
import numpy as np

def nothing(x):
    pass

img = cv2.imread('image_E.png', cv2.IMREAD_GRAYSCALE)
cv2.namedWindow('Gradient Window')

cv2.createTrackbar('Kernel Size', 'Gradient Window', 3, 31, nothing)

while True:
    k_size = cv2.getTrackbarPos('Kernel Size', 'Gradient Window')
    
    if k_size % 2 == 0: k_size += 1
    if k_size < 1: k_size = 1

    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (k_size, k_size))
    result = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)

    cv2.imshow('Gradient Window', result)
    if cv2.waitKey(1) & 0xFF == 27:
        break

cv2.destroyAllWindows()