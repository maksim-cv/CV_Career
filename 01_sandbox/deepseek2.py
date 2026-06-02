import cv2

main = cv2.imread("cat.jpg")
print(main.shape)
main_grey = cv2.imread("cat.jpg", cv2.IMREAD_GRAYSCALE)
print(main_grey.shape)
grey = cv2.cvtColor(main, cv2.COLOR_BGR2GRAY)
print(grey.shape)

cv2.imshow("Origin", main)
cv2.imshow("Origin_grey", main_grey)
cv2.imshow("Grey", grey)
cv2.waitKey(0)
cv2.destroyAllWindows()
