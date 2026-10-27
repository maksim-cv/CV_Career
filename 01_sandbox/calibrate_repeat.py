import cv2

img = cv2.imread('chessboard2.webp')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret, x = cv2.findChessboardCorners(gray, (9, 6), None)
if ret:
    cv2.drawChessboardCorners(img, (9, 6), x, ret)
    cv2.imshow('res', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()