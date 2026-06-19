import cv2
import numpy as np

img = cv2.imread('book2.jpg')
h, w = img.shape[:2]
# Точка 1: (64, 126)
# Точка 2: (387, 52)
# Точка 3: (112, 337)
# Точка 4: (437, 267)
pts1 = np.float32([[64, 126],
                  [387, 52],
                  [112, 337],
                  [437, 267]])
w1 = np.linalg.norm(pts1[1] - pts1[0])
w2 = np.linalg.norm(pts1[3] - pts1[2])

h1 = np.linalg.norm(pts1[2] - pts1[0])
h2 = np.linalg.norm(pts1[3] - pts1[1])

width = max(w1, w2)
height = max(h1, h2)
pts2 = np.float32([[0, 0],
                  [width-1, 0],
                  [0, height-1],
                  [width-1,height-1]])
M = cv2.getPerspectiveTransform(pts1, pts2)
result = cv2.warpPerspective(img, M, (int(width), int(height)))

cv2.imshow('img', img)
cv2.imshow('result', result)
cv2.waitKey(0)
cv2.destroyAllWindows()

