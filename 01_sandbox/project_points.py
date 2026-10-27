import cv2
import numpy as np

# 1. Создаем черный пустой экран размером 640x480 пикселей
img = np.zeros((480, 640, 3), dtype=np.uint8)

# 2. Задаем 3D-точку (X=100, Y=100, Z=1000). Например, 1 метр прямо и чуть вправо-вниз.
point_3d = np.float32([[100, 100, 1000]])

# 3. Задаем матрицу K: фокус = 500 пикселей, оптический центр = (320, 240)
K = np.float32([[500, 0, 320], 
                [0, 800, 240], 
                [0, 0, 1]])

# 4. Идеальная камера: без искажений линзы (dist), без поворота (rvec) и без сдвига (tvec)
dist = np.zeros(4, np.float32)
rvec = np.zeros(3, np.float32)
tvec = np.zeros(3, np.float32)

# 5. Проецируем 3D-точку в 2D-пиксели!
points_2d, _ = cv2.projectPoints(point_3d, rvec, tvec, K, dist)

# 6. Достаем полученные координаты u и v, и рисуем зеленую точку
u, v = int(points_2d[0][0][0]), int(points_2d[0][0][1])
cv2.circle(img, (u, v), 10, (0, 255, 0), -1)

# Выводим результат и печатаем координаты в консоль
print(f"3D точка спроецировалась в пиксель: U={u}, V={v}")
cv2.imshow('Virtual Camera', img)
cv2.waitKey(0)
cv2.destroyAllWindows()