import cv2
import matplotlib.pyplot as plt

face = cv2.imread('face.jpg')
# линзы
cv2.circle(face, (100, 62), 15, (255, 20, 20), -1)
cv2.circle(face, (50, 62), 15, (255, 20, 20), -1)
# переносица
cv2.line(face, (50, 62), (100, 62), (255, 20, 20), 2)
# дужки
cv2.line(face, (35, 62), (25, 20), (255, 20, 20), 2)
cv2.line(face, (115, 62), (125, 20), (255, 20, 20), 2)
# # улыбка
# cv2.line(face, (56, 104), (86, 104), (0, 179, 255)) 
# # уголки 50, 100 95, 100
# cv2.line(face, (56, 104), (50, 100), (0, 179, 255)) 
# cv2.line(face, (86, 104), (95, 100), (0, 179, 255)) 
cv2.ellipse(face, (73, 95), (30, 15), 0, 0, 180, (0, 179, 255), 2)
# текст
text = 'Smile!'
org = (20, 20)
fontFace = cv2.FONT_HERSHEY_DUPLEX 
fontScale = 1
color = (0, 0, 0)
thickness = 1
cv2.putText(face, text, org, fontFace, fontScale, color, thickness)
cv2.imwrite('smile_face.jpg', face)
plt.imshow(face[:, :, ::-1])
plt.show()
# cv2.imshow('face', face)
# cv2.waitKey(0)
# cv2.destroyAllWindows()