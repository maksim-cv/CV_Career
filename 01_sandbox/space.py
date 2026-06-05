import cv2
import numpy as np
import random

space = np.zeros((640, 640, 3))
space = space.astype(np.uint8)
for i in range(100):
    random_pixels_list = random.sample(list(range(1, 640)), 2)
    space[random_pixels_list[0], random_pixels_list[1]] = [255, 255, 255]

space[300:340, 300:340] = [0, 0, 255]
cv2.imwrite("space.jpg", space)
cv2.imshow("space", space)
cv2.waitKey(0)
cv2.destroyAllWindows()
