import cv2

img = cv2.imread('book_vectors.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# blur = cv2.GaussianBlur(gray, (11, 11), 0)
def nothing(x):
    pass
cv2.namedWindow('Trackbar')
# cv2.resizeWindow('Trackbars', 600, 300)  # Ширина, высота\
cv2.createTrackbar('th_min', 'Trackbar', 50, 300, nothing)
cv2.createTrackbar('th_max', 'Trackbar', 150, 900, nothing)
while True:
    th_min = cv2.getTrackbarPos('th_min', 'Trackbar')
    th_max = cv2.getTrackbarPos('th_max', 'Trackbar')
    edge = cv2.Canny(gray, th_min, th_max)
    cv2.imshow('edge', edge)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

