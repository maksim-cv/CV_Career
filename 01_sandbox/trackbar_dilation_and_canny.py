import cv2
import numpy as np

def nothing(x):
    pass

# Загрузка изображения в градациях серого
img = cv2.imread('detection_robot.png', cv2.IMREAD_GRAYSCALE)
if img is None:
    img = np.zeros((300, 300), dtype=np.uint8)
    cv2.putText(img, "No Image", (50, 150), cv2.FONT_HERSHEY_SIMPLEX, 1, 255, 2)

# Применяем Canny с порогами 110 и 171
canny_edges = cv2.Canny(img, 110, 171)

cv2.namedWindow('Dilation Window')
cv2.createTrackbar('Kernel Size', 'Dilation Window', 3, 31, nothing)
cv2.createTrackbar('Iterations', 'Dilation Window', 1, 10, nothing)
cv2.createTrackbar('Canny Low', 'Dilation Window', 110, 255, nothing)
cv2.createTrackbar('Canny High', 'Dilation Window', 171, 255, nothing)

while True:
    k_size = cv2.getTrackbarPos('Kernel Size', 'Dilation Window')
    iterations = cv2.getTrackbarPos('Iterations', 'Dilation Window')
    low = cv2.getTrackbarPos('Canny Low', 'Dilation Window')
    high = cv2.getTrackbarPos('Canny High', 'Dilation Window')
    
    if k_size % 2 == 0: k_size += 1
    if k_size < 1: k_size = 1
    if iterations < 1: iterations = 1

    # Пересчитываем Canny при изменении порогов
    edges = cv2.Canny(img, low, high)
    
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (k_size, k_size))
    result = cv2.dilate(edges, kernel, iterations=iterations)

    cv2.imshow('Canny Edges', edges)
    cv2.imshow('Dilation Window', result)
    
    key = cv2.waitKey(1) & 0xFF
    if key == 27:  # ESC
        break
    elif key == ord('s'):
        cv2.imwrite('dilated_result.jpg', result)
        print("Сохранено как dilated_result.jpg")

cv2.destroyAllWindows()