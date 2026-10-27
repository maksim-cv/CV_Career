# 44. Определить центр масс (центроид) для каждого найденного контура. почитал теорию
import cv2

# 1. Загрузка и перевод в оттенки серого
img = cv2.imread('banana.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 2. Бинаризация (инвертированная, чтобы объект стал белым на черном фоне)
_, bin_img = cv2.threshold(gray, 220, 255, cv2.THRESH_BINARY_INV)

# 3. Поиск контуров
contours, _ = cv2.findContours(bin_img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

if contours:
    # Выбираем самый большой контур (банан)
    cnt = max(contours, key=cv2.contourArea)
    try:
        M = cv2.moments(cnt)
        if M["m00"] != 0:
            cX = int(M["m10"] / M["m00"])
            cY = int(M["m01"] / M["m00"])
            
        # === ПРОВЕРКА РЕЗУЛЬТАТА ===
            cv2.drawContours(img, [cnt], -1, (0, 255, 0), 2)
            # Рисуем центр масс (красная точка)
            cv2.circle(img, (cX, cY), 7, (0, 0, 255), -1)
        print(f"Успех! Центр масс отрисован в координатах: X={cX}, Y={cY}")
    except NameError:
        print("Ошибка: Переменные cX и cY еще не созданы или не рассчитаны.")
else:
    print("Контуры не найдены.")

# 5. Отображение окна с результатом
cv2.imshow('Moments Practice', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
