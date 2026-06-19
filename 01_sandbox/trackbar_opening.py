import cv2
import numpy as np

def nothing(x):
    pass

img = cv2.imread('image_C.png', cv2.IMREAD_GRAYSCALE)
if img is None:
    img = np.zeros((300, 300), dtype=np.uint8)
    cv2.putText(img, "No Image", (50, 150), cv2.FONT_HERSHEY_SIMPLEX, 1, 255, 2)
cv2.namedWindow('Opening Window')

# Для morphologyEx итерации обычно оставляют базовыми, крутим размер ядра
cv2.createTrackbar('Kernel Size', 'Opening Window', 3, 31, nothing)

while True:
    k_size = cv2.getTrackbarPos('Kernel Size', 'Opening Window')
    
    if k_size % 2 == 0: k_size += 1
    if k_size < 1: k_size = 1

    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (k_size, k_size))
    result = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)

    cv2.imshow('Opening Window', result)
    if cv2.waitKey(1) & 0xFF == 27:
        break

cv2.destroyAllWindows()