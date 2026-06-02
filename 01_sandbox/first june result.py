import cv2
import matplotlib.pyplot as plt

img = cv2.imread("cat.jpg")  # ориг цветной если он bgr
grey_1 = cv2.imread("cat.jpg", cv2.IMREAD_GRAYSCALE)  # ч/б (1 способ)
grey_2 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # ч/б (2 способ)
print(f"Размеры цветного: {img.shape}")
print(f"Размеры ч/б: {grey_1.shape}")

plt.figure(1)
plt.imshow(
    img[:, :, ::-1]
)  # переводим в rgb, matplotlib выводит через rgb. При cv2 менять не нужно
plt.title("Оригинал")

plt.figure(2)
plt.imshow(grey_1, cmap="gray")
plt.title("Ч/б вариант 1")

plt.show()
