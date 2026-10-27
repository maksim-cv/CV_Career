import cv2
import numpy as np
#1 картинку загрузил 1 раз
img = cv2.imread('mandarin.jpg')
# cv2.imshow('img', img)
# cv2.imwrite('copy.jpg', img)
print(f'ширина {img.shape[1]}, высота {img.shape[0]}')
#2
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
# cv2.imshow('img', img)
# cv2.imshow('gray', gray)
# cv2.imshow('hsv', hsv)
# #3
# b, g, r = cv2.split(img)
# cv2.imshow('b', b)
# cv2.imshow('g', g)
# cv2.imshow('r', r)
# merged = cv2.merge((b, g, r))
# cv2.imshow('merged', merged)
#4
low = np.uint8([5, 33, 149])
up = np.uint8([255, 255, 255])
mask = cv2.inRange(hsv, low, up)
result = cv2.bitwise_and(img, img, mask=mask)

# cv2.imshow('mask', mask)
# day 2
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
open = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
close = cv2.morphologyEx(open, cv2.MORPH_CLOSE, kernel)
cv2.imshow('close', close)

contours, _ = cv2.findContours(close, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
main_contour = max(contours, key=cv2.contourArea)
# аппроксимируем контур
peri = cv2.arcLength(main_contour, True)
approx_contour = cv2.approxPolyDP(main_contour, 0.002*peri, True)
cv2.drawContours(img, [approx_contour], -1, (255, 0, 0), 3)
x, y, w, h = cv2.boundingRect(approx_contour)
cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 3)
# cv2.imshow('result', result)
cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
