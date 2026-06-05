import cv2

forest = cv2.imread('forest.jpg')
forest_hsv = cv2.cvtColor(forest, cv2.COLOR_BGR2HSV)
h, s, v = cv2.split(forest_hsv)
print(h[h.shape[0]//2, h.shape[1]//2])
cv2.imshow('h', h)
cv2.imshow('s', s)
cv2.imshow('v', v)
cv2.waitKey(0)
cv2.destroyAllWindows()
