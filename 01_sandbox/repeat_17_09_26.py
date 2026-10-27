import cv2
import numpy as np

img = np.zeros((720, 1080), np.uint8)
img2 = np.zeros((720, 1080), np.uint8)
img3 = np.full((720, 1080), 255, dtype=np.uint8)
cv2.imshow('house1', img)
cv2.imshow('house2', img2)
cv2.imshow('house3', img3)
cv2.waitKey(0)
cv2.destroyAllWindows()
import cv2

def load_image_info(path):
    img = cv2.imread(path)
    if img is None:
        return 'Ошибка загрузки'
    else:
        return type(img), img.shape, img.dtype
path = input()
load_image_info(path)

def save_grayscale(src, dst):
    img = cv2.imread(src, cv2.IMREAD_GRAYSCALE)
    x = cv2.imwrite(dst, img)
    print("True" if x is True else 'False')
save_grayscale('book.jpg', 'book_new.jpg')

def swap_red_blue(image):
    img_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    return img_rgb
def extract_roi(img, y1, y2, x1, x2):
    img_new = img.copy()
    roi = img_new[y1:y2, x1:x2]
    return roi

def process_image(img):
    img_new = img.copy()
    roi = img_new[100:400, 200:600]
    flipped = cv2.flip(flipped, 0)
    res = cv2.resize(flipped, (320, 240))
    return res

