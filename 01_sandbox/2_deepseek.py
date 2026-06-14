import cv2

img = cv2.imread('apples.jpg')
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
red_min = 43, 17, 0
red_max = 179, 255, 255

green_min = 33, 0, 0
green_max = 46, 253, 232

mask_red = cv2.inRange(hsv, red_min, red_max)
mask_green = cv2.inRange(hsv, green_min, green_max)
res = cv2.bitwise_and(hsv, hsv, mask=mask_red + mask_green)

result = cv2.cvtColor(res, cv2.COLOR_HSV2BGR)
cv2.imshow('original', img)
cv2.imshow('result', result)
cv2.imwrite('both_apples.jpg', result)
cv2.waitKey(0)
cv2.destroyAllWindows()