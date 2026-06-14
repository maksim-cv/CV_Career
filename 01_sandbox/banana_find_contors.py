import cv2

# 1. Загрузить
img = cv2.imread('banana.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 2. Сделать чёрно-белым
_, bin = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

# 3. Найти контуры
contours, _ = cv2.findContours(bin, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# 4. Нарисовать
out = img.copy()
cv2.drawContours(out, contours, -1, (0,255,0), 3)

# 5. Показать
cv2.imshow('contours', out)
cv2.waitKey(0)

print(len(contours))
cv2.imshow('mask', bin)