import cv2
import numpy as np
"""
#erosion
img = cv2.imread('blackandwhite.jpg',0)
kernel = np.ones((5,5),np.uint8)
erosion = cv2.erode(img,kernel,iterations = 1)
cv2.imshow('cd',erosion)
"""
"""
#dilation
img = cv2.imread('blackandwhite.jpg',0)
kernel = np.ones((5,5),np.uint8)
dilation = cv2.dilate(img,kernel,iterations = 1)
cv2.imshow('cd',dilation)
"""
"""
#opening; erosion followed by dilation
img = cv2.imread('noise.jpg',0)
kernel = np.ones((5,5),np.uint8)
opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
cv2.imshow('cd',opening)
"""
"""
#closing; dilation followed by erosion
img = cv2.imread('blackandwhite.jpg',0)
kernel = np.ones((5,5),np.uint8)
closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
cv2.imshow('cd',closing)
"""
"""
#outline of an object
img = cv2.imread('blackandwhite.jpg',0)
kernel = np.ones((5,5),np.uint8)
gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)
cv2.imshow('cd',gradient)
"""
"""
#difference between input and opening
img = cv2.imread('blackandwhite.jpg',0)
kernel = np.ones((5,5),np.uint8)
tophat = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel)
cv2.imshow('cd',tophat)
"""
"""
#difference between input and closing
img = cv2.imread('blackandwhite.jpg',0)
kernel = np.ones((5,5),np.uint8)
blackhat = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, kernel)
cv2.imshow('cd',blackhat)
"""
cv2.getStructuringElement(cv2.MORPH_RECT,(5,5))
cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))
cv2.getStructuringElement(cv2.MORPH_CROSS,(5,5))
