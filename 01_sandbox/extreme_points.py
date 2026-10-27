import cv2


def get_extreme_points(contour):
    """Возвращает 4 крайние точки контура: (left, right, top, bottom)"""
    left = tuple(contour[contour[:, :, 0].argmin()][0])
    right = tuple(contour[contour[:, :, 0].argmax()][0])
    top = tuple(contour[contour[:, :, 1].argmin()][0])
    bottom = tuple(contour[contour[:, :, 1].argmax()][0])

    return left, right, top, bottom


# --- Пример использования в коде ---
# Допустим, вы нашли контур 'cnt'
left, right, top, bottom = get_extreme_points(cnt)