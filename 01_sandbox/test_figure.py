import cv2
import matplotlib.pyplot as plt

# Загружаем фото
img = cv2.imread("cat.jpg")
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Создаём холст
plt.figure(figsize=(12, 5))

# 1 картинка
plt.subplot(1, 3, 1)
plt.imshow(img_rgb)
plt.title("Оригинал")
plt.axis("off")

# 2 картинка (серый через cvtColor)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
plt.subplot(1, 3, 2)
plt.imshow(gray, cmap="gray")
plt.title("Ч/б (cvtColor)")
plt.axis("off")

# 3 картинка (синий канал)
b, g, r = cv2.split(img)
plt.subplot(1, 3, 3)
plt.imshow(b, cmap="gray")
plt.title("Синий канал")
plt.axis("off")

plt.show()
