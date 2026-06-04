import cv2
import numpy as np

# 2
gray = np.full((10, 10), 128)
color_img = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR).astype(np.uint8)
print(color_img.shape)
for i in range(len(color_img)):
    color_img.itemset(i, i, 2, (0, 0, 255))


cv2.imshow("gray", color_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
