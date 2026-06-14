import cv2
import numpy as np

smile = np.full((800, 800, 3), 255, dtype=np.uint8)

cv2.circle(smile, (400,400), 100, (0, 255, 255), -1)
cv2.line(smile, (450, 450), (350, 350), (40, 180, 150), thickness=2)


cv2.imshow('smile', smile)
cv2.waitKey(0)
cv2.destroyAllWindows()