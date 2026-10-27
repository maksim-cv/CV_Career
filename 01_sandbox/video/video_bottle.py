import cv2
import numpy as np
cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    if not ret:
        break
    else:
        frame = cv2.flip(frame, cv2.ROTATE_180)
        mask = cv2.inRange(frame, np.uint8([0, 87, 36]), np.uint8([145, 255, 161]))
        res = cv2.bitwise_and(frame, frame, mask=mask)
        # cv2.imshow('result', res)
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (11, 11))
        closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel=kernel)
        cv2.imshow('closing', closing)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
cap.release()