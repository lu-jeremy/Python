import cv2
#more efficient way of storing the information of rows and columns;store images
import numpy as np

cap = cv2.VideoCapture(0)

while(1):

    #frame (stored in frame) and whether it was successful or not (stored in underscore variable)
    _, frame = cap.read()

    # Convert BGR to HSV (hue saturated value)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # define range of blue color in HSV
    lower_blue = np.array([45,100,50]) # lowest blue color you want to detect
    #everything between these two colors will be visible, everything else will not be
    upper_blue = np.array([75,255,255]) # highest blue color you want to detect

    # Threshold the HSV image to get only blue colors
    #lower and upper blue range are used to set the 1's or white in the mask, everything else is set to 0
    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    # Bitwise-AND mask and original image
    #result multiplies image; makes all xof the colors other than blue 0, and puts on the frame (destination)
    res = cv2.bitwise_and(frame,frame,mask=mask)

    cv2.imshow('frame',frame)
    cv2.imshow('mask',mask)
    cv2.imshow('res',res)
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
"""
>>> green = np.uint8([[[0,255,0 ]]])
>>> hsv_green = cv2.cvtColor(green,cv2.COLOR_BGR2HSV)
>>> print hsv_green
add 10 to 60 and subtract 10 from 60
[[[ 60 255 255]]]"""
