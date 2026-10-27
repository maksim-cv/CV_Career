import cv2
import numpy as np

img = cv2.imread('book_vectors.png') # изображение не помещается на экране
img2 = img.copy()
h, w = img.shape[:2]
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
canny = cv2.Canny(gray, 200, 600)

kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
dilate = cv2.dilate(canny, kernel)
contours, _ = cv2.findContours(dilate, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
if contours:
    max_c = max(contours, key=cv2.contourArea)
else:
    print('Контуры не найдены')
    exit()

perimeter = cv2.arcLength(max_c, True)
approx = cv2.approxPolyDP(max_c, 0.02 * perimeter, True)
cv2.drawContours(img, [approx], -1, (255, 0, 0), 3)
# [[[188  61]]

#  [[ 98 392]]

#  [[558 491]]

#  [[614 147]]]
approx = approx.reshape((4,2))
pts1 = np.zeros((4, 2), dtype=np.float32)
summ = approx.sum(axis=1)
# print(summ) [ 249  490 1049  761]

pts1[0], pts1[2] = approx[np.argmin(summ)], approx[np.argmax(summ)]

diff = np.diff(approx, axis=1)
pts1[1], pts1[3] = approx[np.argmin(diff)], approx[np.argmax(diff)]
# print(pts_was)
# [[188.  61.]
#  [614. 147.]
#  [558. 491.]
#  [ 98. 392.]]
w1 = np.linalg.norm(pts1[1] - pts1[0])
w2 = np.linalg.norm(pts1[3] - pts1[2])
h1 = np.linalg.norm(pts1[3] - pts1[0])
h2 = np.linalg.norm(pts1[1] - pts1[2])
width = max(w1, w2)
height = max(h1, h2)
pts2 = np.float32([[0, 0], 
                   [width, 0],
                   [width, height],
                   [0, height]])
M = cv2.getPerspectiveTransform(pts1, pts2)
result = cv2.warpPerspective(img2, M, (int(width), int(height)))



cv2.imshow('img', img)
cv2.imshow('dilate', dilate)
cv2.imshow('result', result)
cv2.imwrite('scan_book.png', result)
cv2.waitKey(0)
cv2.destroyAllWindows()
# 1. Получить бинарное изображение (Canny / Threshold / HSV)
# 2. Найти контуры
# 3. Найти нужный контур
# 4. Аппроксимировать до многоугольника
# 5. Получить 4 угла
# 6. Упорядочить углы
# 7. Вычислить размеры выходного изображения
# 8. Сформировать dst
# 9. Получить матрицу через getPerspectiveTransform
# 10. Выполнить warpPerspective

