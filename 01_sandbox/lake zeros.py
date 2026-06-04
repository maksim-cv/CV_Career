import cv2
import matplotlib.pyplot as plt
import numpy as np

lake_bgr = cv2.imread("lake.jpg", cv2.IMREAD_COLOR_RGB)
r, g, b = cv2.split(lake_bgr)
# print(b.shape, lake_bgr.shape) = (182, 277) (182, 277, 3)
zeros = np.zeros_like(lake_bgr)
red_img = cv2.merge()
plt.imshow(lake_bgr)
plt.show()
