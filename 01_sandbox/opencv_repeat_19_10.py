# 1. Загрузить любое изображение с диска и вывести его размерность, тип данных и количество каналов.
import cv2
img1 = cv2.imread('beach.jpg')
print(img1.shape)
print(img1.dtype)
print(img1.ndim)
# 2. Вывести изображение на экран в отдельном окне до нажатия любой клавиши.
import cv2
img1 = cv2.imread('beach.jpg')
cv2.imshow('beach', img1)
cv2.waitKey(0)
cv2.destroyAllWindows()
# 3. Конвертировать цветное изображение в оттенки серого и сохранить результат на диск.
import cv2
img1 = cv2.imread('beach.jpg')
gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
print('SUCCESS' if cv2.imwrite('beach_grey.jpg', gray) else 'ERROR')
# 4. Изменить размер изображения, уменьшив его в два раза по ширине и высоте.
import cv2
img = cv2.imread('beach.jpg')
resized = cv2.resize(img, (img.shape[1] // 2, img.shape[0] // 2))
cv2.imshow('beach2', resized)
cv2.waitKey(0)
cv2.destroyAllWindows()
# 5. Изменить размер изображения до фиксированных значений, например, 800 на 600 пикселей.
import cv2
img = cv2.imread('beach.jpg')
resized = cv2.resize(img, (800, 600))
cv2.imshow('beach2', resized)
cv2.waitKey(0)
cv2.destroyAllWindows()
# 6. Обрезать изображение, оставив только его центральную часть.
import cv2
img = cv2.imread('beach.jpg')
roi_center = img[int(0.3*img.shape[1]):int(0.7*img.shape[0]), int(0.3*img.shape[1]):int(0.7*img.shape[0]), :]
cv2.imshow('beach_roi', roi_center)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 7. Отразить изображение по горизонтали, затем по вертикали.
import cv2
img = cv2.imread('beach.jpg')
flipped_gor = cv2.flip(img, 0)
flipped_vert = cv2.flip(img, 1)
cv2.imshow('beach_flipped', flipped_gor)
cv2.imshow('beach_flipped', flipped_vert)
cv2.waitKey(0)
cv2.destroyAllWindows()
# 8. Повернуть изображение на 90 градусов по часовой стрелке, затем на 180.
import cv2
img = cv2.imread('beach.jpg')
rotated_90 = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
rotated_180 = cv2.rotate(img, cv2.ROTATE_180)
cv2.imshow('rotated_180', rotated_90)
cv2.waitKey(0)
cv2.destroyAllWindows()
# 9. Выделить на изображении прямоугольную область и залить ее сплошным черным цветом.
import cv2
import numpy as np
img = cv2.imread('beach.jpg')
img[200:300, 100:400, :] = np.array([0, 0, 0], dtype=np.uint8)
cv2.imshow('beach', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
# 10. Нарисовать на изображении красную линию толщиной 5 пикселей, зеленый прямоугольник и синий круг.
import cv2
img = cv2.imread('beach.jpg')
cv2.line(img, (200, 300), (100, 400), (0, 0, 255), 5, -1)
cv2.rectangle(img, (500, 700), (100, 600), (0, 255, 0), 5)
cv2.circle(img, (500, 300), 100, (255, 0, 0), -1)
cv2.imshow('beach', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
# 11. Написать на изображении текст «Hello CV» белым цветом.
import cv2
img = cv2.imread('beach.jpg')
cv2.putText(img, 'Hello CV', (400, 400), cv2.FONT_HERSHEY_COMPLEX, 5, (255, 255, 255))
cv2.imshow('beach', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
# 12. Разделить цветное изображение на три отдельных канала (синий, зеленый, красный) и вывести каждый как отдельное ЧБ изображение.
import cv2
img = cv2.imread('beach.jpg')
b, g, r = cv2.split(img)
cv2.imshow('b', b)
cv2.imshow('g', g)
cv2.imshow('r', r)
cv2.waitKey(0)
cv2.destroyAllWindows()
# 13. Поменять местами красный и синий каналы.
import cv2
img = cv2.imread('beach.jpg')
rgb = img[:, :, ::-1]
cv2.imshow('rgb', rgb)
cv2.waitKey(0)
cv2.destroyAllWindows()
# 14. Сложить два разных изображения одинакового размера с равными весами (пополам).
import cv2
img1 = cv2.imread('tree.jpg')
img2 = cv2.imread('mountain.jpg')
res = cv2.addWeighted(img1, 0.5, img2, 0.5, 0)
cv2.imshow('rgb', res)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 15. Сложить два изображения с разными весами (например, 70% первого и 30% второго).
import cv2
img1 = cv2.imread('tree.jpg')
img2 = cv2.imread('mountain.jpg')
res = cv2.addWeighted(img1, 0.7, img2, 0.3, 0)
cv2.imshow('rgb', res)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 16. Изменить яркость изображения, добавив к каждому пикселю фиксированное число.
import cv2
import numpy as np
img = cv2.imread('tree.jpg')
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
h, s, v = cv2.split(hsv)
v = cv2.add(v, 40)
res_hsv = cv2.merge((h, s, v))
res = cv2.cvtColor(res_hsv, cv2.COLOR_HSV2BGR)
cv2.imshow('tree', img)
cv2.imshow('tree+', res)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 17. Изменить контрастность изображения, умножив каждый пиксель на коэффициент.
import cv2
import numpy as np

img = cv2.imread('tree.jpg')

img_cnvrt_scl_abs = cv2.convertScaleAbs(img, None, 2)
cv2.imshow('img_scale_abs', img_cnvrt_scl_abs)
cv2.waitKey(0)
cv2.destroyAllWindows() # подсмотрел полностью, не проходил ранее


# 18. Применить к изображению размытие с разным размером ядра (например, 3 на 3, 11 на 11). # 19. Применить к изображению медианное размытие. # 20. Применить к изображению гауссово размытие. # 21. Использовать двусторонний фильтр для размытия с сохранением границ.
# объединил 4 задания в 1, так удобнее
import cv2
img = cv2.imread('dog.jpg')
img1 = cv2.blur(img, (5, 5))
img2 = cv2.GaussianBlur(img, (3, 3), 0)
img3 = cv2.medianBlur(img, 5)
img4 = cv2.bilateralFilter(img, 12, 150, 150)
cv2.imshow('raccon', img)
cv2.imshow('raccon_blur_def', img1)
cv2.imshow('raccon_gaus', img2)
cv2.imshow('raccon_median', img3)
cv2.imshow('raccon_bilateral', img4)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 22. Применить к изображению выделение границ (оператор Собеля) отдельно по горизонтали и по вертикали.
import cv2
img = cv2.imread('dog.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_horiz = cv2.Sobel(img, cv2.CV_64F, dx=0, dy=1, ksize=3)
img_vertic = cv2.Sobel(img, cv2.CV_64F, dx=1, dy=0, ksize=3)
# Вместо img_all = cv2.Sobel(img, ..., 1, 1) делают так:

sobel_ready_h = cv2.convertScaleAbs(img_horiz)
sobel_ready_v = cv2.convertScaleAbs(img_vertic)
img_all_perfect = cv2.addWeighted(sobel_ready_h, 0.5, sobel_ready_v, 0.5, 0)
sobel_ready = cv2.convertScaleAbs(img_all_perfect)
cv2.imshow('dog_h', sobel_ready_h)
cv2.imshow('dog_v', sobel_ready_v)
cv2.imshow('dog', sobel_ready)
cv2.waitKey(0)
cv2.destroyAllWindows() # подсмотрел полностью, такое не проходил ранее
# 23. Применить к изображению детектор границ Кэнни с разными порогами и сравнить результаты.
import cv2
img = cv2.imread('dog.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
res1 = cv2.Canny(gray, 0, 127)
res2 = cv2.Canny(gray, 127, 255)
res3 = cv2.Canny(gray, 40, 120)
cv2.imshow('res1', res1)
cv2.imshow('res2', res2)
cv2.imshow('res3', res3)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 24. Построить гистограмму яркости для черно-белого изображения.
import cv2
import matplotlib.pyplot as plt
# 24. Построить гистограмму яркости для черно-белого изображения.

img = cv2.imread('dog.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
hist = cv2.calcHist([gray], [0], None, [256], [0, 256])
# 25. Выровнять контраст изображения с помощью эквализации гистограммы.
eq = cv2.equalizeHist(gray)

plt.figure(21)
plt.plot(hist)
plt.title('hist')
plt.grid(True)

plt.figure(22)
plt.hist(eq.ravel(), (256), (0, 256))
plt.title('hist eq')
plt.grid(True)
plt.show()
# 26. Перевести изображение в бинарный вид с помощью фиксированного порога (например, 127).
import cv2
img = cv2.imread('dog.jpg', cv2.IMREAD_GRAYSCALE)
_, binary = cv2.threshold(img, 127, 256, cv2.THRESH_BINARY)
cv2.imshow('binary', binary)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 27. Перевести изображение в бинарный вид с помощью адаптивного порога.
import cv2
img = cv2.imread('dog.jpg', cv2.IMREAD_GRAYSCALE)
interval, binary = cv2.adaptiveThreshold(img, 0, 256, cv2.ADAPTIVE_THRESH_MEAN_C)
print(interval)
cv2.imshow('binary', binary)
cv2.waitKey(0)
cv2.destroyAllWindows() # такое не учил, написал что нашёл
# 28. Перевести изображение в бинарный вид с помощью метода Оцу.
import cv2
img = cv2.imread('dog.jpg', cv2.IMREAD_GRAYSCALE)
interval, binary = cv2.threshold(img, 0, 256, cv2.THRESH_OTSU)
print(interval)
cv2.imshow('binary', binary)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 29-34. Применить к бинарному изображению эрозию дилатацию открытие закрытие Морфологического градиент. Применить к изображению преобразование «черная шляпа» и «белая шляпа» и понять разницу.
import cv2
img = cv2.imread('dog.jpg', cv2.IMREAD_GRAYSCALE)
interval, binary = cv2.threshold(img, 0, 255, cv2.THRESH_OTSU)
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))# забыл только как создать ядро и метод cv2.MORPH_RECT, подсмотрел
erozied = cv2.erode(binary, kernel)
dilat = cv2.dilate(erozied, kernel)
opened = cv2.morphologyEx(dilat, cv2.MORPH_OPEN, kernel)
closed = cv2.morphologyEx(opened, cv2.MORPH_CLOSE, kernel)
gradient = cv2.morphologyEx(closed, cv2.MORPH_GRADIENT, kernel)
white_hat = cv2.morphologyEx(gradient, cv2.MORPH_TOPHAT, kernel)
black_hat = cv2.morphologyEx(white_hat, cv2.MORPH_BLACKHAT, kernel)
cv2.imshow('img', img)
cv2.imshow('all_morphol', black_hat)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 35-36. Найти на бинарном изображении все контуры и нарисовать их на исходном изображении.
import cv2
img = cv2.imread('dog.jpg')
img2 = img.copy()
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blurred = cv2.medianBlur(gray, 5)
retr, binary = cv2.threshold(blurred, 0, 255, cv2.THRESH_OTSU)
cannied = cv2.Canny(blurred, 50, 255)
areas, _ = cv2.findContours(binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE) # все внешние, а как найти даже внутренние не помню
    # image: MatLike,
    # mode: int,
    # method: int,
if areas is not None and len(areas) > 0:
    print('yes')
img2 = cv2.drawContours(img2, areas, -1, (0, 0, 255))
cv2.imshow('blurred', blurred)
cv2.imshow('binary', binary)
cv2.imshow('cannied', cannied)
cv2.imshow('result', img2)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 37. Найти самый большой по площади контур и нарисовать вокруг него ограничивающий прямоугольник.
import cv2
import numpy as np


img = cv2.imread('pepper_cucumber.jpg')
img2 = img.copy()
gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

_, bin = cv2.threshold(gray, 191, 255, cv2.THRESH_BINARY_INV)

img_h, img_w = bin.shape[:2]

areas, _ = cv2.findContours(bin, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
area_max = max(areas, key=cv2.contourArea)
x, y, w, h = cv2.boundingRect(area_max)
cv2.rectangle(img2, (x, y), (x+w, y+h), (255, 0, 0), 5)

cv2.imshow('result', img2)
cv2.waitKey(0)
cv2.destroyAllWindows()
# 38. Найти ограничивающий прямоугольник, который повернут относительно осей (минимальный прямоугольник).
import cv2
import numpy as np

img = cv2.imread('book.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

_, bin = cv2.threshold(gray, 68, 255, cv2.THRESH_BINARY_INV)
contours, _ = cv2.findContours(bin, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
if contours:
    cntr = max(contours, key=cv2.contourArea)
    # находим минимальный прямоугольник
    rect = cv2.minAreaRect(cntr) 
    # 3. ВЫЧИСЛЯЕМ 4 ВЕРШИНЫ (УГЛА) ПРЯМОУГОЛЬНИКА
    box = cv2.boxPoints(rect)
    box = np.intp(box)
    cv2.drawContours(img, [box], 0, (0, 0, 255), 5)

cv2.imshow('res', img)
cv2.waitKey(0)
cv2.destroyAllWindows() # не делал прежде такое, но и не списал подчистую а изучил теорию, посомтрел решение и решил по памяти

# 39. Найти минимальную описывающую окружность для самого большого контура.
import cv2
import numpy as np

# Загрузка изображения
img = cv2.imread('smarties.png')

# Предобработка: размытие и перевод в оттенки серого
blurred = cv2.GaussianBlur(img, (3, 3), 0)
gray = cv2.cvtColor(blurred, cv2.COLOR_BGR2GRAY)

# Бинаризация (инвертированная, чтобы объекты стали белыми на черном фоне)
_, bin_img = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY_INV)

# Поиск внешних контуров
contours, _ = cv2.findContours(bin_img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
print(f"Всего найдено контуров: {len(contours)}")

if contours:
    cntrs = []
    for c in contours:
        # Фильтрация по площади (исключаем мелкий шум)
        if cv2.contourArea(c) > 10:
            cntrs.append(c)
    
    print(f"Контуров после фильтрации: {len(cntrs)}")
    
    # ИСПРАВЛЕНО: Передаем список cntrs напрямую и ставим -1 для отрисовки ВСЕХ контуров
    # cv2.drawContours(img, cntrs, -1, (255, 0, 0), 3)
for cn in cntrs:
    (x,y), radius = cv2.minEnclosingCircle(cn)
    x = int(x)
    y = int(y)
    radius = int(radius)
    cv2.circle(img, (x, y), radius, (0, 255, 0), 2)
# Отображение результата
cv2.imshow('sweets', img)
cv2.waitKey(0)
cv2.destroyAllWindows()


# 40. Вычислить площадь и периметр каждого найденного контура и отфильтровать контуры с площадью меньше заданного значения.
import cv2

# 41. Аппроксимировать контур ломаной линией (упростить форму), уменьшив количество вершин.
import cv2

img = cv2.imread('banana.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# это был трекбар (234 получил)
# def nothing(x):
#     pass
# cv2.namedWindow('Trackbar')
# cv2.createTrackbar('thresh_min', 'Trackbar', 0, 255, nothing) # 234
# cv2.createTrackbar('thresh_max', 'Trackbar', 255, 255, nothing)

# # cv2.createTrackbar('Trackbar', 'approx_min', 0, 255, nothing)
# # cv2.createTrackbar('Trackbar', 'approx_max', 0, 255, nothing)

# while True:
#     thresh_min = cv2.getTrackbarPos('thresh_min', 'Trackbar')
#     thresh_max = cv2.getTrackbarPos('thresh_max', 'Trackbar')
#     _, bin = cv2.threshold(gray, thresh_min, thresh_max, cv2.THRESH_BINARY_INV, cv2.CHAIN_APPROX_SIMPLE)

#     cv2.imshow('banana', bin)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
# cv2.destroyAllWindows()

_, bin = cv2.threshold(gray, 234, 255, cv2.THRESH_BINARY_INV)
contours, _ = cv2.findContours(bin, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
if contours:
    cntr = max(contours, key=cv2.contourArea)
    cnt = cv2.approxPolyDP(cntr, 0.01*cv2.arcLength(cntr, True), True)
        # curve: MatLike,
        # epsilon: float,
        # closed: bool,
    cv2.drawContours(img, [cnt], -1, (240, 30, 70), 2)
    cv2.imshow('sweets', img)
    cv2.waitKey(0)
cv2.destroyAllWindows()

# 42. Выпуклость контура: найти выпуклую оболочку для контура и нарисовать ее. не проходил, че то почитал, но понял так себе
import cv2

# 43. Найти дефекты выпуклости контура. не проходил, че то почитал, но понял так себе
import cv2

# 44. Определить центр масс (центроид) для каждого найденного контура. почитал теорию
import cv2

# 1. Загрузка и перевод в оттенки серого
img = cv2.imread('banana.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 2. Бинаризация (инвертированная, чтобы объект стал белым на черном фоне)
_, bin_img = cv2.threshold(gray, 220, 255, cv2.THRESH_BINARY_INV)

# 3. Поиск контуров
contours, _ = cv2.findContours(bin_img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

if contours:
    # Выбираем самый большой контур (банан)
    cnt = max(contours, key=cv2.contourArea)
    try:
        M = cv2.moments(cnt)
        if M["m00"] != 0:
            cX = int(M["m10"] / M["m00"])
            cY = int(M["m01"] / M["m00"])
            
        # === ПРОВЕРКА РЕЗУЛЬТАТА ===
            cv2.drawContours(img, [cnt], -1, (0, 255, 0), 2)
            # Рисуем центр масс (красная точка)
            cv2.circle(img, (cX, cY), 7, (0, 0, 255), -1)
        print(f"Успех! Центр масс отрисован в координатах: X={cX}, Y={cY}")
    except NameError:
        print("Ошибка: Переменные cX и cY еще не созданы или не рассчитаны.")
else:
    print("Контуры не найдены.")

# 5. Отображение окна с результатом
cv2.imshow('Moments Practice', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 45. Вычислить моменты контура. почитал теорию
import cv2

# 46. Создать маску для объекта на изображении на основе найденного контура.
import cv2

# 47. Вычислить средний цвет объекта, используя его маску.
import cv2

# 48. Применить перспективное преобразование: выделить 4 точки на изображении и «выпрямить» его.
import cv2

# 49. Создать черное изображение и нарисовать на нем несколько заполненных геометрических фигур (круг, квадрат, треугольник) для дальнейшего тестирования алгоритмов.
import cv2

# 50. Создать два бинарных изображения и применить к ним побитовые операции: логическое И, логическое ИЛИ, исключающее ИЛИ и НЕ.
import cv2
