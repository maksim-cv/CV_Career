import cv2

img = cv2.imread('planet.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

x, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
print(f"OTSU нашёл порог: {x}")
contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

if contours:
    result = img.copy()
    max_c = max(contours, key=cv2.contourArea)

cv2.drawContours(result, [max_c], -1, (0, 255, 0), 3)

cv2.imshow('original', img)
cv2.imshow('result', result)

cv2.waitKey(0)
cv2.destroyAllWindows()