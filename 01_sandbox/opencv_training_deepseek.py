import cv2

# 1
cat = cv2.imread("cat.jpg")
print(f"Ширина: {cat.shape[0]}, Высота: {cat.shape[1]}, канальность: {cat.shape[2]}")

cv2.imshow("Оригинал", cat)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 2
img_main = cv2.imread("cat.jpg")
img_gray = cv2.cvtColor(img_main, cv2.COLOR_BGR2GRAY)  # 1 способ
img_gray2 = cv2.imread("cat.jpg", cv2.IMREAD_GRAYSCALE)

cv2.imshow("Ч/б", img_gray)
cv2.imshow("Ч/Б", img_gray2)
cv2.imshow("Оригинал", img_main)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 3
gray_third = cv2.imwrite("result_bw.jpg", img_gray)
print("Сохранено")

cv2.imshow("Ч/Б", gray_third)
cv2.waitKey(0)
cv2.destroyAllWindows()
