import cv2

# Загрузка изображения
image = cv2.imread("dog.jpg")

# Интерактивный выбор ROI
r = cv2.selectROI("Select ROI", image)

# Распаковка координат
x, y, width, height = r

# Выделение и отображение ROI
roi = image[int(y) : int(y + height), int(x) : int(x + width)]
cv2.imshow("Cropped Image", roi)
cv2.waitKey(0)
cv2.destroyAllWindows()
