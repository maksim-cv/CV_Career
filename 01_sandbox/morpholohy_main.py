import cv2
import numpy as np

# 1. Загружаем сгенерированную маску в градациях серого
src = cv2.imread('noisy_square.png', cv2.IMREAD_GRAYSCALE)
if src is None:
    print("Ошибка: не удалось найти файл 'noisy_square.png'. Сначала запусти скрипт генерации.")
    exit()

# 2. Создаем ядра разных размеров под разные задачи
kernel_small = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
kernel_medium = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))

# Шаг А: Убираем белый шум вокруг квадрата с помощью Opening
# Ядро 3x3 идеально подходит, так как внешние точки имеют размер 2x2
step_opening = cv2.morphologyEx(src, cv2.MORPH_OPEN, kernel_small)

# Шаг Б: Закрываем внутренние черные дыры с помощью Closing
# Берем маску после Шага А. Используем ядро 5x5, чтобы надежно "зашить" дыры размером 3x3
step_closing = cv2.morphologyEx(step_opening, cv2.MORPH_CLOSE, kernel_medium)

# Шаг В: Соединяем разорванные края объекта с помощью Dilation
# Создаем большое ядро специально для затягивания глубоких ран на краях
kernel_large = cv2.getStructuringElement(cv2.MORPH_RECT, (11, 11))

# Применяем Дилатацию увеличенным ядром к результату закрытия
step_dilation = cv2.dilate(step_closing, kernel_large)

# 3. Выводим результаты в 4 отдельных окна
cv2.imshow('1. Original Mask (with defects)', src)
cv2.imshow('2. After Opening (External noise removed)', step_opening)
cv2.imshow('3. After Closing (Internal holes fixed)', step_closing)
cv2.imshow('4. After Dilation (Edges reconnected)', step_dilation)

# Ожидаем нажатия любой клавиши, после чего закрываем окна
cv2.waitKey(0)
cv2.destroyAllWindows()