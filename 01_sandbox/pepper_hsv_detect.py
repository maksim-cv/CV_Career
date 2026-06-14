import cv2
import numpy as np

img = cv2.imread('pepper.jpg')
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Красный цвет (два диапазона)
lower_red1 = np.array([0, 50, 50])
upper_red1 = np.array([10, 255, 255])
lower_red2 = np.array([170, 50, 50])
upper_red2 = np.array([180, 255, 255])

mask1 = cv2.inRange(hsv, lower_red1, upper_red1)
mask2 = cv2.inRange(hsv, lower_red2, upper_red2)
mask = cv2.bitwise_or(mask1, mask2)

# Контуры
contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

if contours:
    max_contour = max(contours, key=cv2.contourArea)
    cv2.drawContours(img, [max_contour], -1, (0, 255, 0), 3)

cv2.imshow('result', img)
cv2.waitKey(0)
cv2.destroyAllWindows()