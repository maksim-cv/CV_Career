import numpy as np

# 4 точки, полученные от approxPolyDP (в случайном порядке)
pts_was = np.float32([
    [512, 860],   # точка 0
    [975, 775],   # точка 1
    [943, 359],   # точка 2
    [414, 206]    # точка 3
])
pts1 = np.zeros_like(pts_was)
summ = pts_was.sum(axis=1)
pts1[0], pts1[2] = pts_was[np.argmin(summ)], pts_was[np.argmax(summ)]

diff = np.diff(pts_was, axis=1)
pts1[1], pts1[3] = pts_was[np.argmin(diff)], pts_was[np.argmax(diff)]
# print(pts1)
# [[414. 206.]
#  [943. 359.]
#  [975. 775.]
#  [512. 860.]]