# 37. Найти самый большой по площади контур и нарисовать вокруг него ограничивающий прямоугольник.
import cv2
import numpy as np


img = cv2.imread('pepper_cucumber.jpg')
img2 = img.copy()
gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

_, bin = cv2.threshold(gray, 191, 255, cv2.THRESH_BINARY_INV)

img_h, img_w = bin.shape[:2]

areas, _ = cv2.findContours(bin, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
# valid_areas = []
# if areas:
#     for c in areas:
#         x, y, w, h = cv2.boundingRect(c)
#         if w < img_w * 0.95 and h < img_h * 0.95:
#             valid_areas.append(c)

# if valid_areas:
area_max = max(areas, key=cv2.contourArea)
x, y, w, h = cv2.boundingRect(area_max)
cv2.rectangle(img2, (x, y), (x+w, y+h), (255, 0, 0), 5)

cv2.imshow('result', img2)
cv2.waitKey(0)
cv2.destroyAllWindows()