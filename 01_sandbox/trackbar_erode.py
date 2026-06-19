import cv2
import numpy as np

def nothing(x):
    pass

# Загружаем бинарную маску
img = cv2.imread('image_B.png', cv2.IMREAD_GRAYSCALE)
if img is None:
    img = np.zeros((300, 300), dtype=np.uint8)
    cv2.putText(img, "No Image", (50, 150), cv2.FONT_HERSHEY_SIMPLEX, 1, 255, 2)

cv2.namedWindow('Erosion Window')

# Создаем трекбары: размер ядра (от 1 до 31) и итерации (от 1 to 10)
cv2.createTrackbar('Kernel Size', 'Erosion Window', 3, 31, nothing)
cv2.createTrackbar('Iterations', 'Erosion Window', 1, 10, nothing)

while True:
    k_size = cv2.getTrackbarPos('Kernel Size', 'Erosion Window')
    iterations = cv2.getTrackbarPos('Iterations', 'Erosion Window')
    
    # Защита: размер ядра должен быть нечетным и не равен 0
    if k_size % 2 == 0: k_size += 1
    if k_size < 1: k_size = 1
    if iterations < 1: iterations = 1

    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (k_size, k_size))
    result = cv2.erode(img, kernel, iterations=iterations)

    cv2.imshow('Erosion Window', result)
    
    if cv2.waitKey(1) & 0xFF == 27: # Esc для выхода
        break

cv2.destroyAllWindows()