import cv2
import numpy as np
def nothing(x):
    pass
cv2.namedWindow('trackbar')
cv2.createTrackbar('H min', 'trackbar', 0, 179, nothing)
cv2.createTrackbar('H max', 'trackbar', 0, 179, nothing)

cv2.createTrackbar('S min', 'trackbar', 0, 255, nothing)
cv2.createTrackbar('S max', 'trackbar', 0, 255, nothing)

cv2.createTrackbar('V min', 'trackbar', 0, 255, nothing)
cv2.createTrackbar('V max', 'trackbar', 0, 255, nothing)


img = cv2.imread('fruits.png')
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
while True:
    h_min = cv2.getTrackbarPos('H min', 'trackbar')
    h_max = cv2.getTrackbarPos('H max', 'trackbar')

    s_min = cv2.getTrackbarPos('S min', 'trackbar')
    s_max = cv2.getTrackbarPos('S max', 'trackbar')

    v_min = cv2.getTrackbarPos('V min', 'trackbar')
    v_max = cv2.getTrackbarPos('V max', 'trackbar')
    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])
    mask = cv2.inRange(img, lower, upper)
    result = cv2.bitwise_and(img, img, mask=mask)
    cv2.imshow('result', result)
    cv2.waitKey(1) 
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cv2.destroyAllWindows()


