import cv2

apples = cv2.cvtColor(cv2.imread('apples.jpg'), cv2.COLOR_BGR2HSV)



# Красный
light_red = (0, 127, 220)   # H Min=0, S Min=127, V Min=220
dark_red = (179, 255, 255)  # H Max=179, S Max=255, V Max=255

# Зелёный
light_green = (27, 33, 0)   # H Min=27, S Min=33, V Min=0
dark_green = (150, 255, 255) # H Max=150, S Max=255, V Max=255
mask_green = cv2.inRange(apples, light_green, dark_green)
mask_red = cv2.inRange(apples, light_red, dark_red)
mask = mask_red + mask_green
result = cv2.bitwise_and(apples, apples, mask=mask)
res_bgr = cv2.cvtColor(result, cv2.COLOR_HSV2BGR)

cv2.imshow('res', res_bgr)
cv2.waitKey(0)
cv2.destroyAllWindows()

