import cv2
import numpy as np
img = cv2.imread('planet.png')
h, w = img.shape[:2]
def nothing(x):
    pass
cv2.namedWindow('Trackbar')
cv2.createTrackbar('ось x', 'Trackbar', w//2, w, nothing)
cv2.createTrackbar('ось y', 'Trackbar', h//2, h, nothing)
cv2.createTrackbar('угол', 'Trackbar', 0, 360, nothing)
cv2.createTrackbar('масштаб', 'Trackbar', 1, 5, nothing)
cv2.createTrackbar('сдвиг X', 'Trackbar', 0, w, nothing)
cv2.createTrackbar('сдвиг Y', 'Trackbar', 0, h, nothing)

while True:
    center_w = cv2.getTrackbarPos('ось x', 'Trackbar')
    center_h = cv2.getTrackbarPos('ось y', 'Trackbar')
    angle = cv2.getTrackbarPos('угол', 'Trackbar')
    scale = cv2.getTrackbarPos('масштаб', 'Trackbar')
    x_coor = cv2.getTrackbarPos('сдвиг X', 'Trackbar')
    y_coor = cv2.getTrackbarPos('сдвиг Y', 'Trackbar')
    M1 = cv2.getRotationMatrix2D((center_w, center_h), angle, scale)
    pts1 = np.float32([[0, 0], [w-1, 0], [0, h-1]])
    pts2 = np.float32([[x_coor, y_coor], [w-1, 0], [0, h-1]])
    M2 = cv2.getAffineTransform(pts1, pts2)
    M2 = np.vstack([M2, [0, 0, 1]])
    M = M1 @ M2
    result = cv2.warpAffine(img, M, (w, h))
    cv2.imshow('result', result)
    cv2.imshow('img', img)
    if cv2.waitKey(1) and 0xFF == ord('q'):
        break
cv2.destroyAllWindows()