import cv2
import numpy as np

img = cv2.imread('apple_green.jpg') # яблоко лежит на столе
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# создаем маску
low = 32, 0, 69
up = 179, 255, 255
mask = cv2.inRange(hsv, low, up)
# применяем морфологию (заделываем дыры в центре и убираем лишний шум)
kernel_low = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
kernel_high = cv2.getStructuringElement(cv2.MORPH_RECT, (9, 9))
open = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel_low)
result = cv2.morphologyEx(open, cv2.MORPH_CLOSE, kernel_high)
# границы
contour, _ = cv2.findContours(result, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(gray, [max(contour, key=cv2.contourArea)], -1, (0, 255, 0), 3)
# поворот
result = cv2.flip(result, -1)
# увеличим в 2 раза
result = cv2.resize(result, None, fx=2, fy=2)
#сдвиг на (50;30)
M = np.float32([[1, 0, 50], [0, 1, 30]])
random = cv2.warpAffine(result, M, (300, 300))
cv2.imshow('mask', mask)
cv2.imshow('open', open)
cv2.imshow('close and open', result)
cv2.imshow('random', random)
cv2.imshow('gray', gray)
cv2.waitKey(0)
cv2.destroyAllWindows()

