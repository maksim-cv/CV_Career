import cv2
import matplotlib.pyplot as plt

img = cv2.imread('tree.jpg', cv2.IMREAD_GRAYSCALE)
hist = cv2.calcHist([img], [0], None, [256], [0, 256])

plt.figure(21)
plt.title('hist before')
plt.grid(True)
plt.plot(hist)

equlaized = cv2.equalizeHist(img)

plt.figure(22)
plt.title('hist after')
plt.hist(equlaized.ravel(), 256, [0, 256])
plt.show()