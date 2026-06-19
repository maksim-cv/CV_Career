import cv2
import numpy as np

img = cv2.imread('leasts.jpg')
img = cv2.resize(img, None, fx=0.5, fy=0.5)
# img = cv2.resize(img, img.shape[1] // 2, img.shape[0] // 2) не работает
reversed = cv2.flip(img, 1)

M = np.float32([[1, 0, 50], [0, 1, 30]])
result = cv2.warpAffine(reversed, M, (256, 256))
cv2.imshow('img', img)
cv2.imshow('result', result)
cv2.waitKey(0)
cv2.destroyAllWindows()