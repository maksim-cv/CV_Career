# 38. Найти ограничивающий прямоугольник, который повернут относительно осей (минимальный прямоугольник).
import cv2
import numpy as np

img = cv2.imread('book.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

_, bin = cv2.threshold(gray, 68, 255, cv2.THRESH_BINARY_INV)
contours, _ = cv2.findContours(bin, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
if contours:
    cntr = max(contours, key=cv2.contourArea)
    # находим минимальный прямоугольник
    rect = cv2.minAreaRect(cntr) 
    # 3. ВЫЧИСЛЯЕМ 4 ВЕРШИНЫ (УГЛА) ПРЯМОУГОЛЬНИКА
    box = cv2.boxPoints(rect)
    box = np.intp(box)
    cv2.drawContours(img, [box], 0, (0, 0, 255), 5)

cv2.imshow('res', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
       