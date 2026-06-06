import cv2
import matplotlib.pyplot as plt

t = cv2.imread('tomatoes.jpg')
tomatoes = cv2.cvtColor(t, cv2.COLOR_BGR2HSV)

h, s, v = cv2.split(tomatoes)
# Красный (два диапазона, так как тон зациклен)
light_red1 = (0, 50, 50)
dark_red1 = (10, 255, 255)
light_red2 = (160, 50, 50)
dark_red2 = (180, 255, 255)

# Зелёный
light_green = (40, 50, 50)
dark_green = (80, 255, 255)

mask = cv2.inRange(tomatoes, light_red1, dark_red1) + \
       cv2.inRange(tomatoes, light_red2, dark_red2) + \
       cv2.inRange(tomatoes, light_green, dark_green)
result = cv2.bitwise_and(tomatoes, tomatoes, mask=mask)

res_bgr = cv2.cvtColor(result, cv2.COLOR_HSV2BGR)
cv2.imshow('Before', t)
cv2.imshow('After', res_bgr)

cv2.waitKey(0)
cv2.destroyAllWindows()


