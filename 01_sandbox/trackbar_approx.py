import cv2
import numpy as np

img = cv2.imread('polyangles.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
low = 5, 0, 0
up = 255, 255, 255
mask = cv2.inRange(hsv, low, up)
contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
print(len(contours))
contours = contours[0]
def nothing(x):
    pass
cv2.namedWindow('Trackbar')
cv2.createTrackbar('percent_mistake', 'Trackbar', 0, 100, nothing)
while True:
    result = img.copy()
    value = cv2.getTrackbarPos('percent_mistake', 'Trackbar') / 100
    perimeter = cv2.arcLength(contours, True)
    approx = cv2.approxPolyDP(contours, value * perimeter, True)
    cv2.drawContours(result, [approx], -1, (255, 40, 35), 3)

    cv2.imshow('result', result)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cv2.destroyAllWindows()