import cv2 
import matplotlib.pyplot as plt
import random

wall = cv2.imread('wall.jpg')
graffiti = wall.copy()
visota = graffiti.shape[0] # y
shirina = graffiti.shape[1] # x

print(f'Высота: {visota}, Ширина: {shirina}') # размерность фотографии
# прямоугольник
cv2.rectangle(graffiti, \
              (int(0.2*shirina), int(0.2*visota)), \
                (int(0.8*shirina), int(0.8*visota)), \
                    (255, 0, 0), -1)
# рамка
cv2.rectangle(graffiti, \
              (int(0.18*shirina), int(0.18*visota)), \
                (int(0.82*shirina), int(0.82*visota)), \
                    (0, 0, 240), thickness=8)
cv2.rectangle(graffiti, \
              (int(0.14*shirina), int(0.14*visota)), \
                (int(0.86*shirina), int(0.86*visota)), \
                    (255, 180, 0), thickness=10)
# координаты центров кружков

# кружки
for _ in range(random.choice(range(5, 15))):
    # Сделай так
    x_min = int(0.2 * shirina)   # левая граница прямоугольника
    x_max = int(0.8 * shirina)   # правая граница
    x_coor = random.randint(x_min, x_max)

    y_min = int(0.2 * visota)
    y_max = int(0.8 * visota)
    y_coor = random.randint(y_min, y_max)
    cv2.circle(graffiti, \
               center=(x_coor, y_coor), \
                radius=random.choice(range(20, 80)), \
                    color=(random.choice(range(0, 256)), random.choice(range(0, 256)), random.choice(range(0, 256))), \
                        thickness=-1)


# def circle(
#     img: MatLike,
#     center: Point,
#     radius: int,
#     color: Scalar,
#     thickness: int = ...,
#     lineType: int = ...,
#     shift: int = ...
# текст
# def putText(
#     img: MatLike,
#     text: str,
#     org: Point,
#     fontFace: int,
#     fontScale: float,
#     color: Scalar,
#     thickness: int = ...,
#     lineType: int = ...,
#     bottomLeftOrigin: bool = ...
# ) -> MatLike: ...
text = 'Maksim, Vladyka Mira'

fontFace = cv2.FONT_HERSHEY_DUPLEX 
fontScale = 1.5
color = (0, 0, 0)
thickness = 2

# размеры рамки текста
(shir_ramki, vis_ramki), _ = cv2.getTextSize(text, fontFace, fontScale, thickness)
print(f"Ширина текста: {shir_ramki} px") # Ширина текста: 533 px
print(f"Высота текста: {vis_ramki} px") # Высота текста: 32 px
# def getTextSize(
#     text: str,
#     fontFace: int,
#     fontScale: float,
#     thickness: int

org = (int((shirina - shir_ramki) // 2), int((vis_ramki + visota) // 2))
cv2.putText(graffiti, text, org, fontFace, fontScale, color, thickness)
cv2.imwrite('graffiti.jpg', graffiti)

plt.subplot(121)
plt.title('Before')
plt.imshow(wall[:, :, ::-1])

plt.subplot(122)
plt.title('After')
plt.imshow(graffiti[:, :, ::-1])

plt.show()

