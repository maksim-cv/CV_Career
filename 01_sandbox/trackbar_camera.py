import cv2
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Ошибка: не удалось открыть видеофайл.")
    exit()
def nothing(x):
    pass
cv2.namedWindow('Trackbar')
cv2.createTrackbar('угол', 'Trackbar', 0, 360, nothing)
cv2.createTrackbar('масштаб', 'Trackbar', 1, 5, nothing)
while True:
    _, frame = cap.read()
    frame = cv2.flip(frame, 1)
    h, w = frame.shape[:2]
    angle = cv2.getTrackbarPos('угол', 'Trackbar')
    scale = cv2.getTrackbarPos('масштаб', 'Trackbar')
    M = cv2.getRotationMatrix2D((w//2, h//2), angle, scale)
    result = cv2.warpAffine(frame, M, (w, h))
    cv2.imshow('webka', result)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cv2.destroyAllWindows()
    
