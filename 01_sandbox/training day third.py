import cv2

img = cv2.imread("lake.jpg")
print(img.shape)  # (182, 277, 3)
roi = img[10:100, 20:200].copy()
roi_blur = cv2.GaussianBlur(roi, (5, 5), 0)

cv2.imshow("Original lake", img)

img[10:100, 20:200] = roi_blur

cv2.imshow("Blur lake", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite("lake_blur.jpg", img)

print(img.item(5, 10, 1))
