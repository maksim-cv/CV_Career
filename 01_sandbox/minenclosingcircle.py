import cv2
import numpy as np

# Загрузка изображения
img = cv2.imread('smarties.png')

# Предобработка: размытие и перевод в оттенки серого
blurred = cv2.GaussianBlur(img, (3, 3), 0)
gray = cv2.cvtColor(blurred, cv2.COLOR_BGR2GRAY)

# Бинаризация (инвертированная, чтобы объекты стали белыми на черном фоне)
_, bin_img = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY_INV)

# Поиск внешних контуров
contours, _ = cv2.findContours(bin_img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
print(f"Всего найдено контуров: {len(contours)}")

if contours:
    cntrs = []
    for c in contours:
        # Фильтрация по площади (исключаем мелкий шум)
        if cv2.contourArea(c) > 10:
            cntrs.append(c)
    
    print(f"Контуров после фильтрации: {len(cntrs)}")
    
    # ИСПРАВЛЕНО: Передаем список cntrs напрямую и ставим -1 для отрисовки ВСЕХ контуров
    # cv2.drawContours(img, cntrs, -1, (255, 0, 0), 3)
for cn in cntrs:
    (x,y), radius = cv2.minEnclosingCircle(cn)
    x = int(x)
    y = int(y)
    radius = int(radius)
    cv2.circle(img, (x, y), radius, (0, 255, 0), 2)
# Отображение результата
cv2.imshow('sweets', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
