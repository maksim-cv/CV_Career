import cv2
import numpy as np

img = cv2.imread("book.jpg")

# Точки книги на исходном изображении
src = np.float32([
    [83, 125],   # top-left
    [210, 90],   # top-right
    [136, 308],  # bottom-left
    [261, 270]   # bottom-right
])

# Размер выходного изображения
width = 300
height = 400

# Куда преобразовываем
dst = np.float32([
    [0, 0],
    [width, 0],
    [0, height],
    [width, height]
])

# Матрица перспективного преобразования
M = cv2.getPerspectiveTransform(src, dst)

# Преобразование
warped = cv2.warpPerspective(img, M, (width, height))

cv2.imshow("Original", img)
cv2.imshow("Book", warped)

cv2.waitKey(0)
cv2.destroyAllWindows()