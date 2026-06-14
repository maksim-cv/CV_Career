import cv2
import numpy as np

img = cv2.imread('ball.jpg')
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Диапазоны цветов
blue_min = (118, 161, 0)
blue_max = (123, 255, 255)

yellow_min = (16, 36, 0)
yellow_max = (27, 255, 255)

red_min1 = (0, 50, 50)
red_max1 = (10, 255, 255)
red_min2 = (170, 50, 50)
red_max2 = (180, 255, 255)

# Маски цветов
mask_blue = cv2.inRange(hsv, blue_min, blue_max)
mask_yellow = cv2.inRange(hsv, yellow_min, yellow_max)
mask_red = cv2.inRange(hsv, red_min1, red_max1) + cv2.inRange(hsv, red_min2, red_max2)

# Общая маска
mask = mask_blue + mask_yellow + mask_red

# Применяем маску
res = cv2.bitwise_and(img, img, mask=mask)

# Находим контуры
contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Рисуем самый большой контур
if contours:
    max_contour = max(contours, key=cv2.contourArea)
    cv2.drawContours(img, [max_contour], -1, (0, 255, 0), 3)

# Показываем результат
cv2.imshow('original', img)
cv2.imshow('mask', mask)
cv2.imshow('result', res)

cv2.waitKey(0)
cv2.destroyAllWindows()