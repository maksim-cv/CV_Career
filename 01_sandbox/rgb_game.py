import cv2
import numpy as np

img = np.zeros((500, 500, 3), np.uint8)

def nothing(x):
    pass
cv2.namedWindow('Color')
R = cv2.createTrackbar('R', 'Color', 0, 255, nothing)
G = cv2.createTrackbar('G', 'Color', 0, 255, nothing)
B = cv2.createTrackbar('B', 'Color', 0, 255, nothing)

while True:
    result = img[:]
    r = cv2.getTrackbarPos('R', 'Color')
    g = cv2.getTrackbarPos('G', 'Color')
    b = cv2.getTrackbarPos('B', 'Color')
    cv2.imshow('result', result)
    img[:] = [b, g, r]
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break