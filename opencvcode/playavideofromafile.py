import cv2
import numpy as np
cap = cv2.VideoCapture('output.mjpg')

while cap.isOpened():
    ret, frame = cap.read()
    print(frame)
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
