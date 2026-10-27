import cv2

img = cv2.imread('smarties.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


def nothing(x):
    pass
cv2.namedWindow('Trackbar')
cv2.createTrackbar('x_min', 'Trackbar', 0, 255, nothing)
cv2.createTrackbar('x_max', 'Trackbar', 255, 255, nothing)

while True:
    x_min = cv2.getTrackbarPos('x_min', 'Trackbar')
    x_max = cv2.getTrackbarPos('x_max', 'Trackbar')
    _, binary = cv2.threshold(gray, x_min, x_max, cv2.THRESH_BINARY)
    cv2.imshow('bin', binary)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()