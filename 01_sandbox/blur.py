import cv2

face = cv2.imread("face.jpg")
flower = cv2.imread("flower.jpg")

# Вырезали ROI
roi_face = face[40:70, 40:70]

# Размыли
blur = cv2.GaussianBlur(roi_face, (5, 5), 0)

# Вставили обратно
face[40:70, 40:70] = blur

# Сохранили и показали
cv2.imwrite("face_blurred.jpg", face)
cv2.imshow("Result", face)
cv2.waitKey(0)
cv2.destroyAllWindows()
