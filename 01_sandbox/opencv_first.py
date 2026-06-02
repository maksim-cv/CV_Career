import cv2

# открываем изображение
img_main = cv2.imread("image_cv.jpg", cv2.IMREAD_GRAYSCALE)
img_grayscale = cv2.imread("image_cv.jpg", cv2.IMREAD_GRAYSCALE)
image_unchanged = cv2.imread("image_cv.jpg", cv2.IMREAD_UNCHANGED)

cv2.imshow("Оригинал", img_main)
cv2.imshow("Ч/Б", img_grayscale)
cv2.imshow("ХЗ", image_unchanged)
cv2.waitKey(0)
cv2.destroyAllWindows()
