import cv2

img = cv2.imread('breathing_balls.webp')
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
result = img.copy()
# красные шары
red_low1 = 170, 91, 0
red_high1 = 179, 255, 255
mask_red = cv2.inRange(hsv, red_low1, red_high1)

contours, _ = cv2.findContours(mask_red, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
filtered_red = [c for c in contours if cv2.contourArea(c) > 600]
filtered_red.sort(key=cv2.contourArea, reverse=True)
print(f'Красных шаров: {len(filtered_red)}', end=',') # 2 шара определил почему-то. Шары имеют небольшое белое пространство между собой и не касаются! Но алгоритм определил 3 шара как 1 почему-то
for i in range(len(filtered_red)):
    x, y, w, h = cv2.boundingRect(filtered_red[i])
    cv2.rectangle(result, (x, y), (x+w, y+h), (0, 0, 255), 1)
# желтые шары
yellow_low = 0, 42, 0
yellow_high = 63, 255, 255
mask_yellow = cv2.inRange(hsv, yellow_low, yellow_high)
contours, _ = cv2.findContours(mask_yellow, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
filtered_yellow = [c for c in contours if cv2.contourArea(c) > 600]
filtered_yellow.sort(key=cv2.contourArea, reverse=True)
print(f'Желтых шаров: {len(filtered_yellow)}', end=',') # 3 шара определил почему-то. Шары имеют небольшое белое пространство между собой и не касаются! Но алгоритм определил 3 шара как 1 почему-то
for i in range(len(filtered_yellow)):
    x, y, w, h = cv2.boundingRect(filtered_yellow[i])
    cv2.rectangle(result, (x-2, y-2), (x+w+2, y+h+2), (0, 200, 255), 1)
# синие шары 

blue_low = 84, 12, 0
blue_high = 174, 255, 255
mask_blue = cv2.inRange(hsv, blue_low, blue_high)
contours, _ = cv2.findContours(mask_blue, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
filtered_blue = [c for c in contours if cv2.contourArea(c) > 600]
filtered_blue.sort(key=cv2.contourArea, reverse=True)
print(f'Синих шаров: {len(filtered_blue)}') # здесь определилось верно, хотя расположены по тем же правилам, что и прошлые шары
for i in range(len(filtered_blue)):
    x, y, w, h = cv2.boundingRect(filtered_blue[i])
    cv2.rectangle(result, (x, y), (x+w, y+h), (255, 0, 0), 1)

cv2.imshow('result', result)
# cv2.imshow('mask_red', mask_red1)
# cv2.imshow('mask_yellow', mask_yellow)
# cv2.imshow('mask_blue', mask_blue)

cv2.imwrite('colorful_balls_result.jpg', result)
cv2.waitKey(0)
cv2.destroyAllWindows()

