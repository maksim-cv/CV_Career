import cv2

img = cv2.imread('chessboard2.webp')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret, corners = cv2.findChessboardCorners(gray, (7, 7), None)
if ret:
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)
    corners_find = cv2.cornerSubPix(gray, corners, (11, 11), (-1, -1), criteria)
    cv2.drawChessboardCorners(img, (7, 7), corners_find, ret)
    cv2.imshow('img', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()