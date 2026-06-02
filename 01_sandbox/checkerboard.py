import cv2
import matplotlib.pyplot as plt

cb_img = cv2.imread("checkerboard.png")
# рисуем шашечки
plt.imshow(cb_img)

# выводим шашечки
plt.show()
