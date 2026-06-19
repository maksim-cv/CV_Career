import cv2
import numpy as np

img = cv2.imread('detection_robot.png')
h, w = img.shape[:2]
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

edges = cv2.Canny(gray, 110, 170)
# дилатация
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
dilated = cv2.dilate(edges, kernel)
# контуры
contours, _ = cv2.findContours(dilated, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

if contours:
    con = max(contours, key=cv2.contourArea)
    result = img.copy()

perimeter = cv2.arcLength(con, True)

approx = cv2.approxPolyDP(con, 0.02 * perimeter, True)
# 4 точки
# [[[414 206]]

#  [[512 860]]

#  [[975 775]]

#  [[943 359]]]
cv2.drawContours(result, [approx], -1, (0, 0, 255), 5)
pts1 = np.float32([[414, 206],
                   [943, 359],
                   [975, 775],
                   [512, 860]])
w1 = np.linalg.norm(pts1[1]-pts1[0])
w2 = np.linalg.norm(pts1[3]-pts1[2])
width = int(max(w1, w2))
h1 = np.linalg.norm(pts1[3]-pts1[0])
h2 = np.linalg.norm(pts1[2]-pts1[1])
height = int(max(h1, h2))
pts2 = np.float32([
    [0, 0],          
    [width - 1, 0], 
    [width - 1, height - 1], 
    [0, height - 1] 
])
M = cv2.getPerspectiveTransform(pts1, pts2)
photo = cv2.warpPerspective(img, M, (width, height))
cv2.imwrite('robot_detection3.png', photo)
cv2.imshow('img', img)   
cv2.imshow('photo', photo)  
cv2.waitKey(0)
cv2.destroyAllWindows()