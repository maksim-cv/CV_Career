import cv2
import matplotlib.pyplot as plt

b = cv2.imread('balls.jpg')
balls = cv2.cvtColor(b, cv2.COLOR_BGR2HSV)

# light_red = 356°, 26%, 99% | 355°, 60%, 98% | 0°, 64%, 94%  |  4°, 64%, 92%     (356//2, 26*2.55, 98*2.55) (0//2, 64*2.55, 92*2.55)
# dark_red = 360°, 70%, 95% |  359°, 66%, 95% | 358°, 73%, 97% | 0°, 66%, 91%     (360//2, 73*2.55, 97*2.55) (0//2, 66*2.55, 91*2.55)
# light_red = (178, 66, 250)
# dark_red = (180, 186, 247)
# light_red = (160, 50, 50)   # H ниже
# dark_red = (180, 255, 255)  # H выше, S и V до максимума
# light_red = (150, 30, 30)    # Уменьшили H, S, V
# dark_red = (180, 255, 255)   # Оставили максимум

# Красный цвет в HSV (OpenCV)
# Диапазон 1 (0-10)
# lower_red1 = (0, 50, 50)
# upper_red1 = (10, 255, 255)

# # Диапазон 2 (160-180)
# lower_red2 = (160, 50, 50)
# upper_red2 = (180, 255, 255)
# # Сужаем за счёт S (насыщенности)
# lower_red1 = (0, 100, 50)   # S было 50 → 100
# upper_red1 = (10, 255, 255)

# lower_red2 = (160, 100, 50) # S было 50 → 100
# upper_red2 = (180, 255, 255)


lower_red1 = (0, 100, 50)
upper_red1 = (10, 255, 255)

lower_red2 = (170, 100, 50)
upper_red2 = (180, 255, 255)

# Объединённая маска
mask_red = cv2.inRange(balls, lower_red1, upper_red1) + cv2.inRange(balls, lower_red2, upper_red2)

# mask = cv2.inRange(balls, light_red, dark_red)
result = cv2.bitwise_and(balls, balls, mask=mask_red)
res_bgr = cv2.cvtColor(result, cv2.COLOR_HSV2BGR)
cv2.imshow('Mask red', res_bgr)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite('red_balls.jpg', res_bgr)







