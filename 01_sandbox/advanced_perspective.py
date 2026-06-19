import cv2
import numpy as np

img = cv2.imread("book.jpg")

pts = np.float32([
    [83, 125],
    [210, 90],
    [136, 308],
    [261, 270]
])

# ширина сверху и снизу
w1 = np.linalg.norm(pts[1] - pts[0])
w2 = np.linalg.norm(pts[3] - pts[2])

# высота слева и справа
h1 = np.linalg.norm(pts[2] - pts[0])
h2 = np.linalg.norm(pts[3] - pts[1])

width = int(max(w1, w2))
height = int(max(h1, h2))

dst = np.float32([
    [0, 0],
    [width, 0],
    [0, height],
    [width, height]
])

M = cv2.getPerspectiveTransform(pts, dst)

warped = cv2.warpPerspective(img, M, (width, height))
cv2.imshow('img', img)
cv2.imshow("Book", warped)
cv2.waitKey(0)
cv2.destroyAllWindows()