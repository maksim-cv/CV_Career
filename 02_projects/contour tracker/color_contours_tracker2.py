import cv2

img = cv2.imread('pepper_cucumber.jpg')
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# красный перец
red_low = 1, 0, 0
red_up = 17, 255, 255
# красный перец
green_low = 10, 0, 0
green_up = 179, 173, 187
# маски
mask_red = cv2.inRange(hsv, red_low, red_up)
mask_green = cv2.inRange(hsv, green_low, green_up)
result = img.copy()

# 1 красный помидор

contours1, _ = cv2.findContours(mask_red, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
pepper_max_contour = max(contours1, key=cv2.contourArea)
x1, y1, w1, h1 = cv2.boundingRect(pepper_max_contour)
cv2.rectangle(result, (x1, y1), (x1+w1, y1+h1), (255, 0, 0), 2)
print('Перец: ',  int(cv2.contourArea(pepper_max_contour)), 'пикселей', end=',')

# 2 красный перец

contours2, _ = cv2.findContours(mask_red, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
tomato_max_contour = sorted(contours1, key=cv2.contourArea, reverse=True)[1]
x2, y2, w2, h2 = cv2.boundingRect(sorted(contours1, key=cv2.contourArea, reverse=True)[1])
cv2.rectangle(result, (x2, y2), (x2+w2, y2+h2), (255, 0, 0), 2)
print('Помидор: ',  int(cv2.contourArea(tomato_max_contour)), 'пикселей', end=',')

# 3 зеленый огурец
contours3, _ = cv2.findContours(mask_green, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cucumber_max_contour = max(contours3, key=cv2.contourArea)
x3, y3, w3, h3 = cv2.boundingRect(cucumber_max_contour)
cv2.rectangle(result, (x3, y3), (x3+w3, y3+h3), (0, 165, 255), 2)
print('Огурец: ',  int(cv2.contourArea(cucumber_max_contour)), 'пикселей')

cv2.imshow('result', result)
cv2.imwrite('pepper_cucumber_boxes.jpg', result)
cv2.waitKey(0)
cv2.destroyAllWindows()
