import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('c1.png',0)
def nothing(x):
    pass

cv2.namedWindow('canny')

cv2.createTrackbar('min','canny',0,255,nothing)
cv2.createTrackbar('max','canny',0,255,nothing)

switch = '0 : OFF \n1 : ON'
cv2.createTrackbar(switch, 'canny',0,1,nothing)

while(1):
    maximum = cv2.getTrackbarPos('max','canny')
    minimum = cv2.getTrackbarPos('min','canny')
    """
    print(minimum)
    print(maximum)
    """
    s = cv2.getTrackbarPos(switch,'canny')

    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break
    if s == 0:
        edges = img
    else:
        edges = cv2.Canny(img,minimum,maximum)
    cv2.imshow('img',img)
    cv2.imshow('canny', edges)
cv2.destroyAllWindows()
