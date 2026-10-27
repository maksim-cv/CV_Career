import cv2
import numpy as np

# Один холст 500x500
img1 = np.zeros((500, 500, 3), dtype=np.uint8)
img2 = np.zeros((500, 500, 3), dtype=np.uint8)

# Фигуры пересекаются в зоне (200, 200) -> (250, 250)
cv2.circle(img1, (250, 250), 100, (255, 255, 255), -1)        # Центрированный круг
cv2.rectangle(img2, (200, 200), (350, 350), (255, 255, 255), -1) # Смещенный квадрат
and_ = cv2.bitwise_and(img1, img2)
or_ = cv2.bitwise_or(img1, img2)
xor_ = cv2.bitwise_xor(img1, img2)
not_ = cv2.bitwise_not(img1, img2)
cv2.imshow('img1', img1)
cv2.imshow('img2', img2)

cv2.imshow('and', and_)
cv2.imshow('or_', or_)
cv2.imshow('xor_', xor_)
cv2.imshow('not_', not_)

cv2.waitKey(0)
cv2.destroyAllWindows()
