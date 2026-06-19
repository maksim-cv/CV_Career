import cv2

img = cv2.imread('nature.png')
img = cv2.resize(img, (img.shape[1]//2, img.shape[0]//2))
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

result1 = cv2.Canny(gray, 100, 300)
cv2.imshow('result1', result1)
result2 = cv2.Canny(gray, 50, 150)
cv2.imshow('result2', result2)
result3 = cv2.Canny(gray, 20, 60)
cv2.imshow('result3', result3)
result4 = cv2.Canny(gray, 200, 600)
cv2.imshow('result4', result4)

cv2.waitKey(0)
cv2.destroyAllWindows()