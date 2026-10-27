import cv2
import numpy as np

img = cv2.imread('mandarin.jpg')
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
low = np.uint8([5, 33, 149])
up = np.uint8([255, 255, 255])
mask = cv2.inRange(hsv, low, up)
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
open = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
close = cv2.morphologyEx(open, cv2.MORPH_CLOSE, kernel)
contours, _ = cv2.findContours(close, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
main_contour = max(contours, key=cv2.contourArea)
peri = cv2.arcLength(main_contour, True)
def nothing(x):
    pass 
cv2.namedWindow('Trackbar')
# Трекбар от 0 до 100 (будет означать 0.00 .. 0.10)
cv2.createTrackbar('epsilon', 'Trackbar', 10, 100, nothing)  # 10 = 0.01

while True:
    eps = cv2.getTrackbarPos('epsilon', 'Trackbar') / 1000  # 10 → 0.01
    approx = cv2.approxPolyDP(main_contour, eps * peri, True)
    
    # Отрисовываем на КОПИИ, чтобы не рисовать поверх старого
    img_copy = img.copy()
    cv2.drawContours(img_copy, [approx], -1, (255, 0, 0), 3)
    cv2.imshow('img', img_copy)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break