import numpy as np
import cv2
"""
#find contours
#goes through entire image and finds the points that are same color/intensity
im = cv2.imread('c1.png')
imgray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
ret,thresh = cv2.threshold(imgray,127,255,0)
image, contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
cv2.imshow('image',image)
"""
#draw all contours
img = cv2.imread('c1.png')
imgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret,thresh = cv2.threshold(imgray,107,255,0)
image, contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
print(contours)
img = cv2.drawContours(img, contours, -1, (0,255,0), 3)
cv2.imshow('img',img)
