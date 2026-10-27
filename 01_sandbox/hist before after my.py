import cv2
import matplotlib.pyplot as plt

img = cv2.imread('grid.webp')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
hist = cv2.calcHist([gray], [0], None, [256], [0, 256])

plt.figure(41)
plt.plot(hist)
plt.title('hist before')


plt.figure(42)
plt.imshow(img[:, :, ::-1])
plt.title('img before')


eq = cv2.equalizeHist(gray)

plt.figure(43)
plt.hist(eq.ravel(), 256, (0, 256))
plt.title('hist after')



plt.figure(44)
plt.imshow(eq, cmap='gray')
plt.title('img after')

plt.show()