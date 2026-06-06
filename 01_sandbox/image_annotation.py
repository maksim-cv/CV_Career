import cv2

rocket = cv2.imread('rocket.jpg')
y_main = rocket.shape[0]
x_main = rocket.shape[1]
y_center = y_main//2
x_center = x_main//2
print(y_main, x_main)
cv2.line(rocket, (0,0), (200,200), (0, 0, 255), thickness=10)
cv2.rectangle(rocket, (x_center-50,y_center-50), (x_center+50,y_center+50), (255, 0, 0), 3)
cv2.circle(rocket, (50,50), 40, (0, 255, 0), -1)
cv2.putText(rocket, 'First rocket in space, 19 April, 1961', 
            (50, y_main-50),  # внизу слева
            cv2.FONT_HERSHEY_PLAIN, 1.2, (0, 255, 0), 2)

cv2.imwrite('Rocket in space.png', rocket)

cv2.imshow('rocket', rocket)
cv2.waitKey(0)
cv2.destroyAllWindows()