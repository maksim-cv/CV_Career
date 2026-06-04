import cv2
import numpy as np

# Создаём чёрное изображение 200x200
img = np.zeros((200, 200, 3), dtype=np.uint8)

# Ставим зелёный пиксель (0, 255, 0) в строку 100, столбец 100
img.itemset(100, 100, 0, 0)  # Blue = 0
img.itemset(100, 100, 1, 255)  # Green = 255
img.itemset(100, 100, 2, 0)  # Red = 0

# Читаем значение зелёного канала
green_value = img.item(100, 100, 1)
print(green_value)  # 255

# Для проверки можно сохранить и посмотреть глазками
cv2.imwrite("task1_result.png", img)
