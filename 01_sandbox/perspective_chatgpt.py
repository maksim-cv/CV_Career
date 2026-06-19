import cv2
import numpy as np

# Загружаем изображение
image = cv2.imread('book.jpg')
height, width = image.shape[:2]

# Исходные точки (ваши данные)
pts_src = np.array([[83, 125], [210, 90], [136, 308], [261, 270]], dtype="float32")

# --- Вариант 1: Фиксированный размер (удобно для просмотра) ---
# Вычисляем ширину и высоту книги по расстоянию между углами
w1 = np.linalg.norm(pts_src[0] - pts_src[1])  # верхняя сторона
w2 = np.linalg.norm(pts_src[3] - pts_src[2])  # нижняя сторона
book_width = int(max(w1, w2))

h1 = np.linalg.norm(pts_src[0] - pts_src[3])  # левая сторона
h2 = np.linalg.norm(pts_src[1] - pts_src[2])  # правая сторона
book_height = int(max(h1, h2))

# Целевые точки (прямоугольник)
pts_dst = np.array([
    [0, 0],
    [book_width - 1, 0],
    [book_width - 1, book_height - 1],
    [0, book_height - 1]
], dtype="float32")

# Вычисляем матрицу и применяем преобразование
matrix = cv2.getPerspectiveTransform(pts_src, pts_dst)
result1 = cv2.warpPerspective(image, matrix, (book_width, book_height))

cv2.imwrite('book_corrected_fixed.jpg', result1)
print("✅ Вариант 1 сохранен: book_corrected_fixed.jpg")