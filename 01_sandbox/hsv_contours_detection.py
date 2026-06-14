import cv2

img = cv2.imread('fruits.png')
img = cv2.resize(img, (img.shape[1], img.shape[0] // 2))
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

low = 102, 9, 0
up = 174, 255, 236

mask = cv2.inRange(hsv, low, up)

contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
res_contours = [c for c in contours if cv2.contourArea(c) >= 300]
if res_contours:
    result = img.copy()
    for elem in res_contours:
        cv2.drawContours(result, [elem], -1, (0, 255, 0), 3)
cv2.imshow('result', result)
cv2.imshow('mask', mask)
cv2.waitKey(0)
cv2.destroyAllWindows()