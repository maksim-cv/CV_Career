import cv2
import numpy as np

# Загрузка и уменьшение
img = cv2.imread('pepper.jpg')
h, w = img.shape[:2]
img = cv2.resize(img, (w // 2, h // 2))
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

lower1 = np.array([0, 50, 50])
upper1 = np.array([10, 255, 255])
lower2 = np.array([170, 50, 50])
upper2 = np.array([180, 255, 255])

mask1 = cv2.inRange(hsv, lower1, upper1)
mask2 = cv2.inRange(hsv, lower2, upper2)
mask = cv2.bitwise_or(mask1, mask2)

contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Фильтрация по площади
filtered = [c for c in contours if cv2.contourArea(c) > 1000]

res = img.copy()  # рисуем на BGR копии

if filtered:
    biggest = max(filtered, key=cv2.contourArea)
    cv2.drawContours(res, [biggest], -1, (0, 255, 0), 3)

cv2.imshow('result', res)
cv2.waitKey(0)
cv2.destroyAllWindows()