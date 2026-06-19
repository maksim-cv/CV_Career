import cv2
import numpy as np

img = cv2.imread('elephant.jpg')
h, w = img.shape[:2]

M_rotate1 = cv2.getRotationMatrix2D((w//2, h//2), 150, 0.5)
M_rotate2 = cv2.getRotationMatrix2D((int(w *0.75), int(h *0.75)), -80, 2)
result1 = cv2.warpAffine(img, M_rotate1, (w, h))
result2 = cv2.warpAffine(img, M_rotate2, (w*2, h*2))
# наклон
# 1
pts1 = np.float32([[0, 0], [w-1, 0], [0, h-1]])
# 2
pts2 = np.float32([[0, 0], [w-1, 30], [50, h-1]])
# 3
pts3 = np.float32([[20, 30], [w-20, 50], [5, h-40]])
# 4
pts4 = np.float32([[20, 30], [w-5, 15], [2, h-9]])
M3 = cv2.getAffineTransform(pts1, pts2)
M4 = cv2.getAffineTransform(pts3, pts4)
result3 = cv2.warpAffine(img, M3, (w, h))
result4 = cv2.warpAffine(img, M4, (w*2, h*2))
cv2.imshow('img', img)
# cv2.imshow('result1', result1)
# cv2.imshow('result2', result2)
cv2.imshow('result3', result3)
cv2.imshow('result4', result4)
cv2.waitKey(0)
cv2.destroyAllWindows()