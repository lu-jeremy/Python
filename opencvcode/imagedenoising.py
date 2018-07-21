import numpy as np
import cv2
from matplotlib import pyplot as plt

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

cap = cv2.VideoCapture(0)
while (1):
    #reading video
    res, frame = cap.read()
    #turning into gray
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #going through face cascade 
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    #coordinates and drawing rectangle around face
    for (x,y,w,h) in faces:
        img = cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
        #going through eye cascade and detecting the eyes on the region of interest (the face in this case)
        eyes = eye_cascade.detectMultiScale(roi_gray)
        #creating rectangles around eyes
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
    #showing video
    cv2.imshow('img',frame)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
cv2.destroyAllWindows()
