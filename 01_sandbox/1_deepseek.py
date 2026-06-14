import cv2

img = cv2.imread('lego.jpg')
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
lower = 0, 17, 12
upper = 179, 255, 255
mask = cv2.inRange(hsv, lower, upper)
res = cv2.bitwise_and(hsv, hsv, mask=mask)
result = cv2.cvtColor(res, cv2.COLOR_HSV2BGR)
cv2.imshow('original', img)
cv2.imshow('result', result)
cv2.imwrite('red_lego.jpg', result)
cv2.waitKey(0)
cv2.destroyAllWindows()