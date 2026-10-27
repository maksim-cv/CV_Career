import cv2
import numpy as np

img = cv2.imread('book_with_shadow.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# предобработка
blurred = cv2.medianBlur(gray, (3, 3), 0)
# бинаризация
binary = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
# постобработка
kernel = np.ones((1, 1), dtype=np.uint8)
result = cv2.morphologyEx(binary, cv2.MORPH_OPEN, kernel)

cv2.imshow('img', img)
cv2.imshow('blurred', blurred)
cv2.imshow('binary', binary)
cv2.imshow('result', result)
cv2.waitKey(0)
cv2.destroyAllWindows()