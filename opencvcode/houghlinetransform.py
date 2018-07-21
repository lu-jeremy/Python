import cv2
import numpy as np

img = cv2.imread('mariocoinfull.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray,50,150,apertureSize = 3)
minLineLength = 100
maxLineGap = 10
lines = cv2.HoughLinesP(edges,1,np.pi/180,100,minLineLength,maxLineGap)
newlines = []
for loop_var in lines:
    for var in loop_var:
        print(var)
        newlines.append(var)
for x1,y1,x2,y2 in newlines:
    cv2.line(img,(x1,y1),(x2,y2),(0,255,0),2)
cv2.imshow('houghlines5.jpg',img)
