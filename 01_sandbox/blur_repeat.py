import cv2 
import matplotlib.pyplot as plt
#1
img = cv2.imread('lake.jpg')
roi = img[:50, :50]
img[35:85, 35:85] = roi
cv2.imwrite('lake_roi.jpg', img)

cv2.imshow('roi lake', roi)
cv2.imshow('lake', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
#2
img2 = cv2.imread('face.jpg')
G = cv2.GaussianBlur(img2, (5,5), 0)
m = cv2.medianBlur(img2, 5)
b = cv2.bilateralFilter(img2, d=9, sigmaColor=75, sigmaSpace=75)
# bgb2rgb
G_new = cv2.cvtColor(G, cv2.COLOR_BGR2RGB)
m_new = cv2.cvtColor(m, cv2.COLOR_BGR2RGB)
b_new = cv2.cvtColor(b, cv2.COLOR_BGR2RGB)
img2_new = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)

plt.subplot(141)
plt.title('Gauss blur')
plt.imshow(G_new)

plt.subplot(142)
plt.title('median blur')
plt.imshow(m_new)

plt.subplot(143)
plt.title('bilateralFilter blur')
plt.imshow(b_new)

plt.subplot(144)
plt.title('Origin')
plt.imshow(img2_new)

plt.show()


