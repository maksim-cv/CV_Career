import cv2

img1 = cv2.imread('umbrella.jpg')
img2 = cv2.imread('pepper.jpg')

pepper = cv2.resize(img2, (736, 588))
summa = cv2.add(img1, pepper)
Weight = cv2.addWeighted(img1, 0.8, pepper, 0.5, 0)
difference1 = cv2.subtract(img1, pepper)
difference2 = cv2.subtract(pepper, img1)

cv2.imshow('summa', summa)
cv2.imshow('difference1', difference1)
cv2.imshow('Weight', Weight)
cv2.imshow('difference2', difference2)
cv2.waitKey(0)
cv2.destroyAllWindows()
