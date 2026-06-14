import cv2

cap = cv2.VideoCapture(0)
cap.set(3, 500)
cap.set(4, 300)
if not cap.isOpened():
    print("Ошибка: камера не найдена")
    exit()
while True:
    success, img = cap.read()
    cv2.imshow('Res', img)

    if cv2.waitKey(30) & 0xFF == ord('q'):
        break
