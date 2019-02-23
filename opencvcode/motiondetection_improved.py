import cv2
import time

"""
Notes

webscraping
sentiment analysis
tensor flow

https://js.tensorflow.org/


"""
cap = cv2.VideoCapture(0)

"""
frame = cv2.cvtColor(cap.read()[1], cv2.COLOR_RGB2GRAY)
ret, frame = cv2.threshold(frame,127,255,cv2.THRESH_BINARY)


frame1 = cv2.cvtColor(cap.read()[1], cv2.COLOR_RGB2GRAY)
ret, frame1 = cv2.threshold(frame1,127,255,cv2.THRESH_BINARY)


frame2 = cv2.cvtColor(cap.read()[1], cv2.COLOR_RGB2GRAY)
ret, thresh = cv2.threshold(frame2,127,255,cv2.THRESH_BINARY)
"""

frame1 = None




time.sleep(3)
while True:
    ret, frame2 = cap.read()
    gray2 = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.GaussianBlur(gray2, (21, 21), 0)
 #   ret,thresh = cv2.threshold(gray2, 150,255,cv2.THRESH_BINARY)
    if frame1 is None:
      frame1 = gray2
 #   frame = frame1
   # frame1 = thresh  

    var = cv2.absdiff(frame1, gray2)
    ret, var = cv2.threshold(var,60,255,cv2.THRESH_BINARY)
    var = cv2.dilate(var, None, iterations=2)
    #RETR_EXTERNAL makes the inside of the countour ingnored
    image, contours, hierarchy = cv2.findContours(var,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    if len(contours) != 0:
      c = max(contours, key = cv2.contourArea)

      (x, y, w, h) = cv2.boundingRect(c)
      cv2.rectangle(frame2, (x, y), (x + w, y + h), (0, 255, 0), 2)

    cv2.imshow('frame2',frame2)
    cv2.imshow('var',var)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
cv2.destroyAllWindows()

