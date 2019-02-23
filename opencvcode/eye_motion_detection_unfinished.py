import cv2
import matplotlib.pyplot as plt
import time

cap = cv2.VideoCapture(0)

eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

frame1 = None

time.sleep(3)
while True:
    ret, frame2 = cap.read()
    gray2 = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.GaussianBlur(gray2, (21, 21), 0)

    if frame1 is None:
        frame1 = gray2

    var = cv2.absdiff(frame1, gray2)

    ret, var = cv2.threshold(var, 60, 255, cv2.THRESH_BINARY)
    
    var = cv2.dilate(var, None, iterations=2)
    
    eyes = eye_cascade.detectMultiScale(frame2)
    for (eye_x, eye_y, eye_w, eye_h) in eyes:
        cv2.rectangle(frame2,(eye_x, eye_y),(eye_x + eye_w, eye_y + eye_h),
        (0,255,0),2)
        
    cv2.imshow('frame2',frame2)

    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
cv2.destroyAllWindows()
