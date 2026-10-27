import cv2
import numpy as np


img = cv2.imread('grid.webp')
img = cv2.resize(img, (img.shape[1]//2, img.shape[0]//2))
cv2.imshow('img', img)

# 17. Изменить контрастность изображения, умножив каждый пиксель на коэффициент.
img_cnvrt_scl_abs = cv2.convertScaleAbs(img, None, 2)
# h, s, v = cv2.split(cv2.cvtColor(img, cv2.COLOR_BGR2HSV))
img_v_add = cv2.add(img, 50)
cv2.imshow('img_scale_abs', img_cnvrt_scl_abs)
cv2.imshow('img_v_add', img_v_add)
cv2.waitKey(0)
cv2.destroyAllWindows()
#     src: MatLike,
#     dst: MatLike | None = ...,
#     alpha: float = ...,
#     beta: float = ...

