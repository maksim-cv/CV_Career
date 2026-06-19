import cv2

img = cv2.imread('gear.png', cv2.IMREAD_GRAYSCALE)
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (13, 13))
result = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)

cv2.imshow('result', result)
cv2.waitKey(0)
cv2.destroyAllWindows()