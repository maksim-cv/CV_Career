import cv2
import numpy as np

img = cv2.imread('boat.jpg')
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
# 0, 0, 0
# 37, 17, 255
# Нижний диапазон красного (от темно-красного до ярко-красного)
lower_red1 = np.array([0, 50, 50])
upper_red1 = np.array([10, 255, 255])

# Верхний диапазон красного (от малинового/бордового до чисто красного)
lower_red2 = np.array([170, 50, 50])
upper_red2 = np.array([180, 255, 255])
mask1 = cv2.inRange(hsv, lower_red1, upper_red1)
mask2 = cv2.inRange(hsv, lower_red2, upper_red2)
thresh = cv2.bitwise_or(mask1, mask2)
res1 = cv2.bitwise_and(img, img, mask=thresh)
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
thresh_morph = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)

contour, _ = cv2.findContours(thresh_morph, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
if contour:
    print(len(contour))
    cntr = max(contour, key=cv2.contourArea)
    # cv2.drawContours(img, [cntr], -1, (255, 0, 0), 3)
    # cv2.drawContours(thresh_morph, [cntr], -1, (255, 0, 0), 3)
    x, y, w, h = cv2.boundingRect(cntr)
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 3)
    M = cv2.moments(cntr)
    cX = int(M["m10"] / M["m00"])
    cY = int(M["m01"] / M["m00"])
    cv2.circle(img, (cX, cY), 2, (0, 255, 0), -1)
cv2.imshow('thresh', thresh)
cv2.imshow('res', res1)
cv2.imshow('thresh_morph', thresh_morph)
cv2.imshow('img', img)

cv2.waitKey(0)
cv2.destroyAllWindows()
