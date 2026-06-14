import cv2

img = cv2.imread('orange.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
low = 0, 49, 215
up = 179, 255, 255

x, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY+ cv2.THRESH_OTSU)
contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
print(x)
if contours:
    result = img.copy()
    cv2.drawContours(result, [max(contours, key=cv2.contourArea)], contourIdx=-1, color=(0, 255, 0), thickness=3)
    cv2.imshow('result', result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
