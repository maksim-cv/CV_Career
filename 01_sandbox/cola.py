import cv2
import matplotlib.pyplot as plt

cola_bgr = cv2.imread("coca-cola.png")
cola_rgb = cv2.cvtColor(cola_bgr, cv2.COLOR_BGR2RGB)
#          ниже numpy-специфичная конструкция:
#    (:) — взять каждый элемент по порядку,
# (::-1) — взять каждый элемент, но в обратном порядке.
coke_img_channels_reversed = cola_bgr[:, :, ::-1]

plt.imshow(coke_img_channels_reversed)
plt.imshow(cola_rgb)
plt.show()
