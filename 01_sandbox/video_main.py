import cv2

cap = cv2.VideoCapture('video/Dragon lore -3.mp4')\

while True:
    success, img = cap.read()
    cv2.imshow('Res', img)

    if cv2.waitKey(30) & 0xFF == ord('q'):
        break
