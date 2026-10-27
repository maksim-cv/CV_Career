import cv2
import numpy as np

img = cv2.imread('chessboard2.webp')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

obj = np.zeros((7*7, 3), dtype=np.float32)
obj[:, :2] = np.mgrid[0:7, 0:7].T.reshape(-1, 2)
print(obj)

points_2D = np.zeros(1)
points_3D = np.zeros(1)