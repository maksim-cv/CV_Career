import cv2

img = cv2.imread('planet.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

_, binary = cv2.threshold(gray, 140, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

boundary, _ = cv2.findContours(binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
max_countour = max(boundary, key=cv2.contourArea)
result = img.copy()
cv2.drawContours(result, [max_countour], -1, (0, 255, 255), 3)

cv2.imshow('res', result)
cv2.waitKey(0)
cv2.destroyAllWindows()