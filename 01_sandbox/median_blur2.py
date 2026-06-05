import cv2

space = cv2.imread('space.jpg')
space_new = cv2.medianBlur(space, 5)

cv2.imshow('space_new', space_new)
cv2.imshow('space', space)
cv2.waitKey(0)
cv2.destroyAllWindows()