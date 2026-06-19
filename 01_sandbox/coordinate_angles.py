import cv2

# Глобальные переменные для хранения точек
points = []

def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:  # Левая кнопка мыши
        points.append((x, y))
        print(f"Точка {len(points)}: ({x}, {y})")
        
        # Рисуем кружок в месте клика
        cv2.circle(img, (x, y), 5, (0, 255, 0), -1)
        cv2.imshow('Image', img)

# Загружаем картинку
img = cv2.imread('book2.jpg')
cv2.imshow('Image', img)
cv2.setMouseCallback('Image', click_event)

cv2.waitKey(0)
cv2.destroyAllWindows()

# После закрытия окна выведи все точки
print("\nВсе точки:", points)