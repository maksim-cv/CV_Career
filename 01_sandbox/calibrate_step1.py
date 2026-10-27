import cv2

# 1. Загружаем одно тестовое изображение и переводим его в ч/б
img = cv2.imread('chessboard.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 2. Пытаемся найти внутренние углы шахматной сетки (размер 9х6)
ret, corners = cv2.findChessboardCorners(gray, (9, 6), None)

# 3. Если нашли — рисуем их на цветной картинке и показываем. Иначе — выводим ошибку.
if ret:
    cv2.drawChessboardCorners(img, (9, 6), corners, ret)
    cv2.imshow('Chessboard', img)
    cv2.waitKey(0)
else:
    print("Углы не найдены. Проверьте размер сетки или путь к файлу!")

cv2.destroyAllWindows()