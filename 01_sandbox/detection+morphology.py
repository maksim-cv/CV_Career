import cv2
import numpy as np

# 1. Загрузка изображения
img = cv2.imread('smarties.png')
# Предотвращаем падение, если картинка слишком большая
img = cv2.resize(img, (800, 600)) if img.shape[1] > 1000 else img
output = img.copy()

# 2. Перевод в HSV и фильтрация по НАСЫЩЕННОСТИ (S)
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Вырезаем всё, что имеет яркий цвет (S от 50 до 255). 
# Белый фон и серые тени автоматически станут черными (0).
lower_vivid = np.array([0, 50, 40])
upper_vivid = np.array([180, 255, 255])
raw_mask = cv2.inRange(hsv, lower_vivid, upper_vivid)

# 3. МОРФОЛОГИЧЕСКАЯ ОЧИСТКА

# Шаг А: Убираем дыры внутри конфет (шум)
# Используем круглое ядро, так как конфеты обычно округлые
kernel_round = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
mask_no_holes = cv2.morphologyEx(raw_mask, cv2.MORPH_CLOSE, kernel_round)

# Шаг Б: Разделяем слипшиеся границы
# Эрозия уменьшит объекты и уничтожит тонкие мостики между ними
kernel_separate = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (13, 13))
mask_separated = cv2.erode(mask_no_holes, kernel_separate)

# 4. ПОИСК КОНТУРОВ И ОТРИСОВКА
contours, _ = cv2.findContours(mask_separated, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

for cnt in contours:
    # Игнорируем случайный мелкий мусор
    if cv2.contourArea(cnt) < 300:
        continue
        
    # Считаем центр масс (координаты конфеты)
    M = cv2.moments(cnt)
    if M['m00'] != 0:
        cx = int(M['m10'] / M['m00'])
        cy = int(M['m01'] / M['m00'])
        
        # Так как эрозия уменьшила маску, bounding box вокруг cnt будет чуть меньше реальной конфеты.
        # Для компенсации можно слегка расширить полученные координаты x, y, w, h
        x, y, w, h = cv2.boundingRect(cnt)
        padding = 5
        x = max(0, x - padding)
        y = max(0, y - padding)
        w += padding * 2
        h += padding * 2
        
        # Рисуем рамку и центр
        cv2.rectangle(output, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.circle(output, (cx, cy), 5, (0, 0, 255), -1)

# 5. Вывод окон для дебага пайплайна
cv2.imshow('1. Original', img)
cv2.imshow('2. Raw Mask (No Shadows!)', raw_mask)
cv2.imshow('3. Cleaned & Separated Mask', mask_separated)
cv2.imshow('4. Final Detection', output)

cv2.waitKey(0)
cv2.destroyAllWindows()