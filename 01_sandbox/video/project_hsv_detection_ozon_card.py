import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break
    else:
        # отзеркаливание
        frame = cv2.flip(frame, cv2.ROTATE_180)
        # создание маски
        low = np.uint8([95, 0, 0])
        up = np.uint8([179, 132, 83])
        mask = cv2.inRange(frame, low, up)
        # морфология
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
        morph = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel=kernel)
        # bounding box
        contour, _ = cv2.findContours(morph, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        result = cv2.bitwise_and(frame, frame, mask=mask)
        if contour:
            cntr = max(contour, key=cv2.contourArea)
            x, y, w, h = cv2.boundingRect(cntr)
            # рисуем ограничивающий прямоугольник 
            cv2.rectangle(result, (x, y), (x+w, y+h), (0, 0, 255), 3)
            cv2.rectangle(morph, (x, y), (x+w, y+h), (0, 0, 255), 3)
            # аппроксимируем контур
            peri = 0.02
            approxed = cv2.approxPolyDP(cntr, 0.02 * cv2.arcLength(cntr, True), True)
            # рисуем контур
            cv2.drawContours(result, [cntr], -1, (0, 255, 0), 3)
            # центроид находим
            M = cv2.moments(approxed)
            # Проверяем, что площадь объекта не равна нулю, чтобы не получить ZeroDivisionError
            if M["m00"] != 0:
                cx = int(M["m10"] / M["m00"])
                cy = int(M["m01"] / M["m00"])
                cv2.circle(result, (cx, cy), 3, (0, 0, 255))
        # выводим результат
        cv2.imshow('mask', mask)
        cv2.imshow('morph', morph)
        cv2.imshow('result', result)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
cap.release()

