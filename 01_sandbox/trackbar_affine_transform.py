import cv2
import numpy as np

img = cv2.imread('elephant.jpg')
h, w = img.shape[:2]

def nothing(x):
    pass

cv2.namedWindow('Trackbar')
cv2.createTrackbar('X_coor', 'Trackbar', 0, w - 1, nothing)
cv2.createTrackbar('Y_coor', 'Trackbar', 0, h - 1, nothing)
cv2.createTrackbar('X_coor_0', 'Trackbar', 0, w - 1, nothing)
cv2.createTrackbar('Y_coor_0', 'Trackbar', 0, h - 1, nothing)

while True:
    x_coor = cv2.getTrackbarPos('X_coor', 'Trackbar')
    y_coor = cv2.getTrackbarPos('Y_coor', 'Trackbar')
    x_coor_0 = cv2.getTrackbarPos('X_coor_0', 'Trackbar')
    y_coor_0 = cv2.getTrackbarPos('Y_coor_0', 'Trackbar')
    pts1 = np.float32([[x_coor_0, y_coor_0], [w-1, 0], [0, h-1]])
    pts2 = np.float32([[x_coor, y_coor], [w-1, 0], [0, h-1]])
    M = cv2.getAffineTransform(pts1, pts2)
    result = cv2.warpAffine(img, M, (w, h))
    
    cv2.imshow('result', result)
    if cv2.waitKey(1) and 0xFF == ord('q'):
        break
cv2.destroyAllWindows()
