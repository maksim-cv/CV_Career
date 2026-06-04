import cv2
import matplotlib.pyplot as plt

lake = cv2.imread("lake.jpg")
b, g, r = cv2.split(lake)
# output
plt.figure(figsize=[13, 8])
plt.subplot(141)
plt.title("Red channel")
plt.imshow(r, cmap="gray")

plt.subplot(142)
plt.title("Green channel")
plt.imshow(g, cmap="gray")

plt.subplot(143)
plt.title("Blue channel")
plt.imshow(b, cmap="gray")

lake_merged = cv2.merge((r, g, b))
plt.subplot(144)
plt.title("Merged")
plt.imshow(lake_merged)

plt.show()
