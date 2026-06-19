import cv2
import numpy as np

img = cv2.imread('detection_robot.png')
cv2.imshow('img', img)
h, w = img.shape[:2]
# cv2.imshow('img', img)
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# размытие (не принесло результата)
# blur = cv2.bilateralFilter(img, 13, 75, 75)
# cv2.imshow('blur', blur)

# canny тоже не сработало как нужно
# canny = cv2.Canny(gray, 50, 150)

# hsv маска
low = np.array([25, 0, 48])
up = np.array([179, 255, 168])
mask = cv2.inRange(hsv, low, up)
color = cv2.bitwise_and(img, img, mask=mask)
gray = cv2.cvtColor(color, cv2.COLOR_BGR2GRAY)
# морфология (ни один из методов не сделал лучше, в каждом из них размывался шрихкод, если роботу шрихкод не нужен, тогда приносит эффект)
# kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
# dilated = cv2.dilate(gray, kernel)
# контуры
contour, _ = cv2.findContours(gray, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
if contour:
    contour_main = max(contour, key=cv2.contourArea)
# создаем контур
cv2.drawContours(color, [contour_main], -1, (255, 0, 0), 3)
peri = cv2.arcLength(contour_main, True)

approx = cv2.approxPolyDP(contour_main, 0.02 * peri, True)
side = approx.reshape(4, 2).astype(np.float32)
# [[368 155]
#  [479 909]
#  [993 801]
#  [946 313]]
pts = np.float32([
    [368, 155],  # левый-верхний
    [946, 313],  # правый-верхний
    [993, 801],  # правый-нижний
    [479, 909]   # левый-нижний
])
# ширина сверху и снизу
w1 = np.linalg.norm(pts[1] - pts[0])
w2 = np.linalg.norm(pts[3] - pts[2])

# высота слева и справа
h1 = np.linalg.norm(pts[3] - pts[0])  # Левый край: от Левого-Нижнего (3) до Левого-Верхнего (0)
h2 = np.linalg.norm(pts[2] - pts[1])  # Правый край: от Правого-Нижнего (2) до Правого-Верхнего (1)

width = int(max(w1, w2))
height = int(max(h1, h2))

dst = np.float32([
    [0, 0],           # 1. Левый-верхний (TL)
    [width, 0],       # 2. Правый-верхний (TR)
    [width, height],  # 3. Правый-нижний (BR) <--- Вот так!
    [0, height]       # 4. Левый-нижний (BL)  <--- Вот так!
])

M = cv2.getPerspectiveTransform(pts, dst)

result = cv2.warpPerspective(img, M, (width, height))
cv2.imwrite('robot_detection2.png', result)


cv2.imshow('result', result)
cv2.waitKey(0)
cv2.destroyAllWindows()
