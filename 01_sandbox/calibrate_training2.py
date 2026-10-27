import cv2

img = cv2.imread('chessboard2.webp')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret, corners = cv2.findChessboardCorners(gray, (7, 7))
if ret:
    cv2.drawChessboardCorners(img, (7, 7), corners, ret)
    cv2.imshow('Chessboard', img)
    cv2.waitKey(0)
else:
    print("Углы не найдены. Проверьте размер сетки или путь к файлу!")

cv2.destroyAllWindows()    