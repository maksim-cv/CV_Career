import cv2
import time

# Загружаем изображение
img = cv2.imread('car.jpg', cv2.IMREAD_GRAYSCALE)

# Бинаризация
_, binary = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

# ==========================
# CHAIN_APPROX_NONE
# ==========================
start = time.perf_counter()

contours_none, _ = cv2.findContours(
    binary,
    cv2.RETR_EXTERNAL,
    cv2.CHAIN_APPROX_NONE
)

time_none = time.perf_counter() - start

points_none = sum(len(cnt) for cnt in contours_none)

# ==========================
# CHAIN_APPROX_SIMPLE
# ==========================
start = time.perf_counter()

contours_simple, _ = cv2.findContours(
    binary,
    cv2.RETR_EXTERNAL,
    cv2.CHAIN_APPROX_SIMPLE
)

time_simple = time.perf_counter() - start

points_simple = sum(len(cnt) for cnt in contours_simple)

# Результаты
print(f'CHAIN_APPROX_NONE:')
print(f'  Контуров: {len(contours_none)}')
print(f'  Точек:    {points_none}')
print(f'  Время:    {time_none:.6f} сек\n')

print(f'CHAIN_APPROX_SIMPLE:')
print(f'  Контуров: {len(contours_simple)}')
print(f'  Точек:    {points_simple}')
print(f'  Время:    {time_simple:.6f} сек')