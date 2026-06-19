import cv2

img = cv2.imread('smarties.png', cv2.IMREAD_GRAYSCALE)
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (11, 11))
result1 = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
result2 = cv2.morphologyEx(result1, cv2.MORPH_OPEN, kernel)


cv2.imshow('result', result2)
cv2.waitKey(0)
cv2.destroyAllWindows()
