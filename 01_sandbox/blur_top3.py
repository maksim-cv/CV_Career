import cv2

face_main = cv2.imread("face2.jpg")
print(face_main.shape)
# 1

blur = cv2.blur(face_main, (30, 30))

Gblur = cv2.GaussianBlur(face_main, (9, 9), sigmaX=0)
picture_median = cv2.imread("median_blur.jpg")
Mblur = cv2.medianBlur(picture_median, 9)
Bblur = cv2.bilateralFilter(face_main, 9, 75, 75)

cv2.imshow("1", blur)
cv2.imshow("G", Gblur)
cv2.imshow("M", Mblur)
cv2.imshow("B", Bblur)
cv2.waitKey(0)
cv2.destroyAllWindows()
