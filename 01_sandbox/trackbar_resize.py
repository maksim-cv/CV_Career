import cv2

img = cv2.imread('nature.png')
def nothing(x):
    pass
cv2.namedWindow('Trackbar')
cv2.createTrackbar('fx', 'Trackbar', 1, 10, nothing)
cv2.createTrackbar('fy', 'Trackbar', 1, 10, nothing)

while True:
    fx = cv2.getTrackbarPos('fx', 'Trackbar')
    fy = cv2.getTrackbarPos('fy', 'Trackbar')
    result = cv2.resize(img, None, fx=fx, fy=fy)
    cv2.imshow('result', result)
    cv2.imshow('img', img)
    if cv2.waitKey(1) and 0xFF == ord('q'):
        break
cv2.destroyAllWindows()