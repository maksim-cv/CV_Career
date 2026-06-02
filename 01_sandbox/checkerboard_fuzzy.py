import cv2
import matplotlib.pyplot as plt

# Читаем картинку как чб
cb_img_fuzzy = cv2.imread("checkerboard_fuzzy.jpg")

# Печатаем массив
print(cb_img_fuzzy)

# Показываем картинку
plt.imshow(cb_img_fuzzy, cmap="gray")
plt.show()
