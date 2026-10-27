import cv2
import numpy as np

cap = cv2.VideoCapture(0)
print(f'Ширина: {cap.get(cv2.CAP_PROP_FRAME_WIDTH)}, высота: {cap.get(cv2.CAP_PROP_FRAME_HEIGHT)}, фпс: {cv2.CAP_PROP_FPS}б кадров: {cv2.CAP_PROP_FRAME_COUNT}')
# while True:
#     ret, frame = cap.read()
#     if cv2.waitKey(25) & 0xFF == ord('q'):
#         break