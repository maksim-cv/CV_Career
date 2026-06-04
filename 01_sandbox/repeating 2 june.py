import cv2
import matplotlib.pyplot as plt

img = cv2.imread("flower.jpg")  # BGR
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # RGB
grey_bgr = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # BGR gray
grey = cv2.cvtColor(grey_bgr, cv2.COLOR_GRAY2RGB)  # RGB gray
cv2.imwrite(filename="flower_copy.jpg", img=img)
# 1 способ вывода (требует rgb)
plt.subplot(121)
plt.title("Original flower")
plt.imshow(img_rgb)

plt.subplot(122)
plt.title("Grey flower")
plt.imshow(grey)
plt.show()
# 2 способ вывода (требует bgr)
cv2.imshow("Original flower", img)
cv2.imshow("Grey flower", grey_bgr)
cv2.waitKey(0)
cv2.destroyAllWindows()
