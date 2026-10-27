import cv2
import matplotlib.pyplot as plt
# 24. Построить гистограмму яркости для черно-белого изображения.

img = cv2.imread('dog.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
hist = cv2.calcHist([gray], [0], None, [256], [0, 256])
# 25. Выровнять контраст изображения с помощью эквализации гистограммы.
eq = cv2.equalizeHist(gray)

plt.figure(21)
plt.plot(hist)
plt.title('hist')
plt.grid(True)

plt.figure(22)
plt.hist(eq.ravel(), (256), (0, 256))
plt.title('hist eq')
plt.grid(True)
plt.show()