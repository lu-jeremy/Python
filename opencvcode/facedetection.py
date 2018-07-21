import numpy as np
import cv2
from matplotlib import pyplot as plt

#detect cat face for still pictures, see if it works for Diamond
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
profile_cascade = cv2.CascadeClassifier('haarcascade_profileface.xml')
profile_cascade = cv2.CascadeClassifier('haarcascade_frontalcatface.xml')
#cap = cv2.VideoCapture(0)
img = cv2.imread('cat.jpeg')
while (1):
    #reading video
    #res, frame = cap.read()
    #turning into gray
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #going through face cascade 
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    profile = profile_cascade.detectMultiScale(gray, 1.3, 5)
    #coordinates and drawing rectangle around face
    for (x,y,w,h) in faces:
        img1 = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        #going through eye cascade and detecting the eyes on the region of interest (the face in this case)
        eyes = eye_cascade.detectMultiScale(roi_gray)
        #creating rectangles around eyes
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
    for (px,py,pw,ph) in profile:
            cv2.rectangle(img,(px,py),(px+pw,py+ph),(0,255,0),2)
    #showing video
    cv2.imshow('img',img)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
cv2.destroyAllWindows()
