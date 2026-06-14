import cv2

img = cv2.imread('planet.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)



cv2.imshow('original', img)
cv2.imshow('result', result)

cv2.waitKey(0)
cv2.destroyAllWindows()