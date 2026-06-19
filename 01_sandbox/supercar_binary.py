import cv2

img = cv2.imread('supercar.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

_, binary = cv2.threshold(gray, 20, 255, cv2.THRESH_BINARY )
contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

max_con = max(contours, key=cv2.contourArea)

result = img.copy()
cv2.drawContours(result, [max_con], -1, (0,255,0), 3)
cv2.imshow('orig', binary)
cv2.imshow('after', result)
cv2.waitKey(0)
cv2.destroyAllWindows()
# + cv2.THRESH_OTSU