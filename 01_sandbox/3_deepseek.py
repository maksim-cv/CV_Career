import cv2

img = cv2.imread('ball.jpg')
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
blue_min = 118, 161, 0
blue_max = 123, 255, 255

yellow_min = 16, 36, 0
yellow_max = 27, 255, 255

red_min = 2, 19, 0
red_max = 6, 255, 255

mask = cv2.inRange(hsv, blue_min, blue_max) + cv2.inRange(hsv, yellow_min, yellow_max) + cv2.inRange(hsv, red_min, red_max)

res = cv2.bitwise_and(hsv, hsv, mask=mask)
result = cv2.cvtColor(res, cv2.COLOR_HSV2BGR)
result_gray = cv2.cvtColor(res, cv2.COLOR_BGR2GRAY) 
_, binary_blue = cv2.threshold(result_gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
contours, _ = cv2.findContours(binary_blue, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
result_gray = img.copy()
cv2.drawContours(result_gray, [max(contours, key=cv2.contourArea)], -1, (255, 0, 0), 6)
cv2.imshow('original', img)
cv2.imshow('result', result)
cv2.waitKey(0)
cv2.destroyAllWindows()
print(f"Маска ненулевых: {cv2.countNonZero(binary_blue)}")