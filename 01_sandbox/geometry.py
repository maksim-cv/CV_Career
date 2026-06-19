import cv2
import numpy as np

img = cv2.imread('dog.jpg')
h, w = img.shape[:2]
result = img.copy()
result = cv2.resize(result, None, fx=0.5, fy=0.5)
M_rotate = cv2.getRotationMatrix2D((w//2, h//2), 30, 1)
result = cv2.warpAffine(result, M_rotate, (w, h))
M = np.float32([[1, 0, 50], [0, 1, 30]])
result = cv2.warpAffine(result, M, (w, h))
pts1 = np.float32([[0, 0], [w-1, 0], [0, h-1]])
pts2 = np.float32([[30, 30], [w-1, 0], [0, h-1]])
M_transform = cv2.getAffineTransform(pts1, pts2)
result = cv2.warpAffine(result, M_transform, (w, h))
cv2.imshow('result', result)
cv2.waitKey(0)
cv2.destroyAllWindows()


