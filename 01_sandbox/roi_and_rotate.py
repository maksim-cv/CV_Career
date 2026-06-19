import cv2

fruits = cv2.imread('fruits.png')
fruits = cv2.resize(fruits, None, fx=0.5, fy=0.5)
dog = cv2.imread('dog.jpg')
h_dog, w_dog = dog.shape[:2]
h_fruits, w_fruits = fruits.shape[:2]
M = cv2.getRotationMatrix2D((w_dog//2, h_dog//2), 45, 0.5)
result_dog = cv2.warpAffine(dog, M, (w_dog, h_dog))
fruits[h_fruits-h_dog:h_fruits, w_fruits-w_dog:w_fruits, :] = result_dog
cv2.imshow('result', fruits)
cv2.waitKey(0)
cv2.destroyAllWindows()


