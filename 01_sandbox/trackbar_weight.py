import cv2

planet = cv2.imread('planet.png')
b = cv2.imread('tennis_ball.jpg')
ball = cv2.resize(b, (220, 278))
# по умолчанию
# w1, w2, c = 1, 1, 0
def nothing(x):
    pass
cv2.namedWindow('Weight')
cv2.createTrackbar('w1', 'Weight', 5, 10, nothing)   # 0..10
cv2.createTrackbar('w2', 'Weight', 5, 10, nothing)
cv2.createTrackbar('c', 'Weight', 0, 20, nothing)

while True:
    w1 = cv2.getTrackbarPos('w1', 'Weight') / 10.0   # 5 → 0.5
    w2 = cv2.getTrackbarPos('w2', 'Weight') / 10.0
    c = cv2.getTrackbarPos('c', 'Weight') - 10       # 0..20 → -10..10

    result = cv2.addWeighted(planet, w1, ball, w2, c)
    cv2.imshow('result', result)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()