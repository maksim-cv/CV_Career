import cv2
import matplotlib.pyplot as plt

lake_bgr = cv2.imread("lake.jpg")
b, g, r = cv2.split(lake_bgr)
lake_marged_bgr = cv2.merge((b, g, r))
lake_merged_rgb = cv2.cvtColor(lake_marged_bgr, cv2.COLOR_BGR2RGB)
cv2.imwrite("red_lake.jpg", r)
# вывод

plt.subplot(221)
plt.title("Оригинал (RGB)")
plt.imshow(lake_merged_rgb)

plt.subplot(222)
plt.title("Red Channel")
plt.imshow(r, cmap="grey")

plt.subplot(223)
plt.title("Green Channel")
plt.imshow(g, cmap="grey")

plt.subplot(224)
plt.title("Blue Channel")
plt.imshow(b, cmap="grey")

plt.show()
