import cv2
import numpy as np

# Создаём специальное тестовое изображение
img = np.zeros((400, 600, 3), dtype=np.uint8)
img[:] = (100, 100, 100)  # серый фон

# Рисуем резкую границу
img[200:250, :] = (200, 50, 50)  # красная полоса

# Рисуем шум "соль и перец" (белые точки)
for _ in range(500):
    x, y = np.random.randint(0, 600), np.random.randint(0, 400)
    img[y, x] = (255, 255, 255)

# Рисуем мелкую текстуру (шахматная доска)
for i in range(0, 200, 20):
    for j in range(0, 400, 20):
        img[i : i + 10, j + 400 : j + 410] = (0, 200, 200)  # бирюзовые квадраты

cv2.imwrite("test_original.jpg", img)

# Применяем три метода
gauss = cv2.GaussianBlur(img, (15, 15), 0)
median = cv2.medianBlur(img, 5)
bilateral = cv2.bilateralFilter(img, 9, 75, 75)

cv2.imwrite("1_gaussian.jpg", gauss)
cv2.imwrite("2_median.jpg", median)
cv2.imwrite("3_bilateral.jpg", bilateral)

print("Готово! Открой три файла рядом и сравни:")
print("- 1_gaussian.jpg")
print("- 2_median.jpg")
print("- 3_bilateral.jpg")
