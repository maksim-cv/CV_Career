import cv2

img = cv2.imread('orange.jpg')
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
low = 0, 49, 215
up = 179, 255, 255
mask = cv2.inRange(hsv, low, up)

contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
max_c = max(contours, key=cv2.contourArea)
x, y, w, h = cv2.boundingRect(max_c)
if contours:
    result = img.copy()
    cv2.drawContours(result, [max_c], contourIdx=-1, color=(0, 255, 0), thickness=3)
    cv2.rectangle(result, (x, y), (x+w, y+h), (255, 0, 0), 2) # сделал чтобы потренироваться
    cv2.imshow('result', result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
