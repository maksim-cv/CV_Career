import cv2

img = cv2.imread('chessboard2.webp')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret, corners = cv2.findChessboardCorners(gray, (7, 7), None)
if ret:
    cv2.drawChessboardCorners(img, (7, 7), corners, ret)
    cv2.imshow('img', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()