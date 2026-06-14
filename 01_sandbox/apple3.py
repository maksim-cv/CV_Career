import cv2

b = cv2.imread('apple_green.jpg')
ball = cv2.cvtColor(b, cv2.COLOR_BGR2HSV)
lower_yellow = (32, 0, 62)
upper_yellow = (179, 236, 255)
mask = cv2.inRange(ball, lower_yellow, upper_yellow)
result = cv2.bitwise_and(ball, ball, mask=mask)
results = cv2.cvtColor(result, cv2.COLOR_HSV2BGR)
cv2.imshow('apple', results)
cv2.waitKey(0)
cv2.destroyAllWindows()