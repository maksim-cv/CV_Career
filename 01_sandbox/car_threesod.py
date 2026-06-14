import cv2

car = cv2.imread('car.jpg')
grey = cv2.cvtColor(car, cv2.COLOR_BGR2GRAY)

_, binary = cv2.threshold(grey, 140, 255, cv2.THRESH_BINARY_INV)

contours, _ = cv2.findContours(binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

max_con = max(contours, key=cv2.contourArea)

result = car.copy()
cv2.drawContours(result, [max_con], -1, (255, 0, 0), 3)
cv2.imshow("binary", binary)
cv2.imshow('orig', car)
cv2.imshow('after', result)
cv2.waitKey(0)
cv2.destroyAllWindows()