import cv2
import matplotlib.pyplot as plt

# 1. Загружаем изображение в черно-белом режиме (Grayscale)
img = cv2.imread('beach.jpg', cv2.IMREAD_GRAYSCALE)

# 2. ПРИМЕНЯЕМ МАГИЮ ОДНОЙ СТРОЧКИ — выравнивание гистограммы
img_equalized = cv2.equalizeHist(img)

# 3. Считаем гистограммы для обоих изображений
hist_before = cv2.calcHist([img], [0], None, [256], [0, 256])
hist_after = cv2.calcHist([img_equalized], [0], None, [256], [0, 256])

# 4. Визуализируем результаты через Matplotlib
plt.figure(figsize=(12, 8))

# --- ЛЕВАЯ СТОРОНА: Исходное состояние ---
plt.subplot(2, 2, 1)
plt.title("1. Исходное изображение")
plt.imshow(img, cmap='gray')
plt.axis('off')

plt.subplot(2, 2, 2)
plt.title("2. Исходная гистограмма (ваша)")
plt.plot(hist_before, color='black')
plt.xlim([0, 256])

# --- ПРАВАЯ СТОРОНА: После обработки ---
plt.subplot(2, 2, 3)
plt.title("3. Результат Equalization")
plt.imshow(img_equalized, cmap='gray')
plt.axis('off')

plt.subplot(2, 2, 4)
plt.title("4. Выровненная гистограмма")
plt.plot(hist_after, color='blue')
plt.xlim([0, 256])

plt.tight_layout()
plt.show()
