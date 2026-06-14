import cv2

img = cv2.imread('camera.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

_, binary = cv2.threshold(gray, 240, 255, cv2.THRESH_BINARY_INV)
contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

cv2.drawContours(img, [max(contours, key=cv2.contourArea)], -1, (255, 0, 127), 2)

cv2.imshow('original', img)

cv2.waitKey(0)
cv2.destroyAllWindows()
# + cv2.THRESH_OTSU