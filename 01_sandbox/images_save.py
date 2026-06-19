import cv2
import numpy as np

# Создаем 5 пустых черных матриц 200x200
images = {name: np.zeros((200, 200), dtype=np.uint8) for name in ['A', 'B', 'C', 'D', 'E']}

# Картинка A: Разорванная рамка
cv2.rectangle(images['A'], (50, 50), (150, 150), 255, 4)
images['A'][40:160, 90:110] = 0
images['A'][90:110, 40:160] = 0

# Картинка B: "Гантеля"
cv2.circle(images['B'], (80, 100), 45, 255, -1)
cv2.circle(images['B'], (120, 100), 45, 255, -1)

# Картинка C: Квадрат и мусор
cv2.rectangle(images['C'], (60, 60), (140, 140), 255, -1)
np.random.seed(42)
noise_x = np.random.randint(0, 200, 150)
noise_y = np.random.randint(0, 200, 150)
images['C'][noise_y, noise_x] = 255
cv2.rectangle(images['C'], (60, 60), (140, 140), 255, -1) # Очищаем сам квадрат, чтобы шум был только снаружи

# Картинка D: Дырявый круг
cv2.circle(images['D'], (100, 100), 70, 255, -1)
holes_x = np.random.randint(40, 160, 200)
holes_y = np.random.randint(40, 160, 200)
for x, y in zip(holes_x, holes_y):
    if (x - 100)**2 + (y - 100)**2 < 60**2: # Дыры только внутри круга
        images['D'][y:y+3, x:x+3] = 0

# Картинка E: Сплошная звезда
pts = np.array([[100, 30], [120, 80], [180, 80], [130, 110], [150, 170], 
                [100, 130], [50, 170], [70, 110], [20, 80], [80, 80]], np.int32)
cv2.fillPoly(images['E'], [pts], 255)

# Сохраняем каждое изображение под соответствующим названием
for name, img in images.items():
    filename = f"image_{name}.png"  # Можно использовать .jpg, .bmp и т.д.
    success = cv2.imwrite(filename, img)
    if success:
        print(f"✅ Изображение {name} сохранено как {filename}")
    else:
        print(f"❌ Ошибка при сохранении {name}")

# Вывод на экран
for name, img in images.items():
    cv2.imshow(f"{name}", img)

print("\nВсе изображения сохранены в текущую директорию!")
cv2.waitKey(0)
cv2.destroyAllWindows()