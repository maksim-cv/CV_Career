import cv2
import numpy as np

# 1. Загрузка и уменьшение размера (чтобы влезло на экран)
img = cv2.imread('smarties.png')
img = cv2.resize(img, (800, 600))
output = img.copy()

# 2. Перевод в HSV и цветовая фильтрация (ищем СИНИЙ цвет)
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
lower_blue = np.array([100, 100, 50])
upper_blue = np.array([140, 255, 255])
mask = cv2.inRange(hsv, lower_blue, upper_blue)

# --- БЛОК МОРФОЛОГИИ ---
# Убираем мелкий шум (блики на столе)
kernel_open = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
mask_cleaned = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel_open)

# Зашиваем дырки внутри самих объектов (тени или надписи на крышечках)
kernel_close = cv2.getStructuringElement(cv2.MORPH_RECT, (11, 11))
mask_cleaned = cv2.morphologyEx(mask_cleaned, cv2.MORPH_CLOSE, kernel_close)
# -----------------------

# 3. Поиск контуров на ОЧИЩЕННОЙ маске
# RETR_EXTERNAL - берем только внешние контуры, CHAIN_APPROX_SIMPLE - сжимаем точки
contours, hierarchy = cv2.findContours(mask_cleaned, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# 4. Анализ контуров
for cnt in contours:
    # Игнорируем слишком маленькие контуры (остатки мусора)
    area = cv2.contourArea(cnt)
    if area < 500:
        continue
        
    # Получаем координаты ограничивающего прямоугольника
    x, y, w, h = cv2.boundingRect(cnt)
    cv2.rectangle(output, (x, y), (x + w, y + h), (0, 255, 0), 2)
    
    # Вычисляем центр масс объекта
    M = cv2.moments(cnt)
    if M['m00'] != 0:
        cx = int(M['m10'] / M['m00'])
        cy = int(M['m01'] / M['m00'])
        
        # Рисуем центр и пишем координаты
        cv2.circle(output, (cx, cy), 5, (0, 0, 255), -1)
        cv2.putText(output, f"X:{cx} Y:{cy}", (x, y - 10), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

# Выводим результаты
cv2.imshow('1. Original', img)
cv2.imshow('2. Raw Mask', mask)
cv2.imshow('3. Cleaned Mask', mask_cleaned)
cv2.imshow('4. Detections', output)

cv2.waitKey(0)
cv2.destroyAllWindows()