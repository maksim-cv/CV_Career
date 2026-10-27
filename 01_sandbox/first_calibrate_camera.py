import numpy as np
import cv2
import glob

CHESSBOARD = (9, 6)
objp = np.zeros((CHESSBOARD[0] * CHESSBOARD[1], 3), dtype=np.float32)
objp[:, :2] = np.mgrid[0:CHESSBOARD[0], 0:CHESSBOARD[1]].T.reshape(-1, 2)

points_2D = []
points_3D = []
image = glob.glob('images_chess/*.jpg')
for filename in image:
    img = cv2.imread(filename)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, corners = cv2.findChessboardCorners(img, (CHESSBOARD[0], CHESSBOARD[1]), None)
    if ret:
        criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_COUNT, 30, 0.001)
        result = cv2.cornerSubPix(gray, corners, (5,5), (-1, -1), criteria)
        points_3D.append(objp)
        points_2D.append(result)
ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(objectPoints=points_3D, imagePoints=points_2D, imageSize=gray.shape[::-1], cameraMatrix=None, distCoeffs=None)

# 1. Проверяем общую ошибку
print(f"Ошибка репроекции (RMS): {ret:.4f} пикселей (Ожидаем < 1.0)")

# 2. Проверяем центр кадра (для примера возьмем картинку 1920x1080)
h, w = gray.shape[:2]
print(f"Идеальный центр: {w/2}, {h/2} | Полученный: {mtx[0,2]:.1f}, {mtx[1,2]:.1f}")

# 3. Проверяем фокус
print(f"Разница фокусных расстояний fx и fy: {abs(mtx[0,0] - mtx[1,1]):.2f} (Ожидаем близко к 0)")

# 4. Проверяем тангенциальное искажение
print(f"Тангенциальное искажение p1, p2: {dist[0][2]:.5f}, {dist[0][3]:.5f} (Ожидаем около 0.0)")

