    # 38. Найти ограничивающий прямоугольник, который повернут относительно осей (минимальный прямоугольник).
import cv2
import numpy as np


img = cv2.imread('bike.webp')
img = img.resize((img.shape[1] // 2, img.shape[0] // 2))
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, bin = cv2.threshold(gray, 156, 255, cv2.THRESH_BINARY_INV)
contour, _ = cv2.findContours(bin, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
if contour:
    cnt_clear = []
    for c in contour:
        if cv2.contourArea(c) > 50:
            cnt_clear.append(c)
print(len(cnt_clear))
print(len(contour))

cv2.drawContours(img, contour, 0, (0, 255, 0))

cv2.imshow('result', img)
cv2.waitKey(0)
cv2.destroyAllWindows()


