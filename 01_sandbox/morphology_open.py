import cv2
#1
img = cv2.imread('noisy_square.png', cv2.IMREAD_GRAYSCALE)
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (7, 7))

result1 = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
result2 = cv2.morphologyEx(result1, cv2.MORPH_CLOSE, kernel)

cv2.imshow('result', result2)
cv2.waitKey(0)
cv2.destroyAllWindows()
