import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while (1):
    _,frame = cap.read()
    
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_green = np.array([50,100,100])
    upper_green = np.array([70,255,255])
    lower_blue = np.array([25,100,50])
    upper_blue = np.array([95,255,255])
    lower_red = np.array([-10,100,100])
    upper_red = np.array([10,255,255])
    
    mask1 = cv2.inRange(hsv, lower_red, upper_red)
    
    mask2 = cv2.inRange(hsv, lower_green, upper_green)
    
    mask3 = cv2.inRange(hsv, lower_blue, upper_blue)
    
    res1 = cv2.bitwise_and(frame, frame, mask=mask1)
    res2 = cv2.bitwise_and(frame, frame, mask=mask2)
    res3 = cv2.bitwise_and(frame, frame, mask=mask3)
    
    final_image = cv2.add(res1,res2,res3)

    cv2.imshow('finalimage',final_image)
    cv2.imshow('frame',frame)
    cv2.imshow('mask',mask1)
    cv2.imshow('mask2',mask2)
    cv2.imshow('mask',mask3)
    if cv2.waitKey(5) & 0xFF == 27:
        break
cv2.destroyAllWindows()
"""
#[[[ 60 255 255]]] 70 50
#[[[120 255 255]]] 110 130
#[[[  0 255 255]]]10 -10


green = np.uint8([[[0,255,0 ]]])
hsv_green = cv2.cvtColor(green,cv2.COLOR_BGR2HSV)
print(hsv_green)
blue = np.uint8([[[255,0,0 ]]])
hsv_blue = cv2.cvtColor(blue,cv2.COLOR_BGR2HSV)
print(hsv_blue)
red = np.uint8([[[0,0,255]]])
hsv_red = cv2.cvtColor(red,cv2.COLOR_BGR2HSV)
print(hsv_red)
#add 10 to 60 and subtract 10 from 60
"""

