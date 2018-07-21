import numpy as np
import cv2
#use erode to get rid of noise 
"""
cap = cv2.VideoCapture(0)

fgbg = cv2.bgsegm.createBackgroundSubtractorGMG()

while(1):
    ret, frame = cap.read()

    fgmask = fgbg.apply(frame)

    cv2.imshow('frame',fgmask)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
"""
cap = cv2.VideoCapture(0)



while(1):
    ret, frame = cap.read()
    kernel = np.ones((5,5),np.uint8)

    fgbg = cv2.bgsegm.createBackgroundSubtractorMOG()
    fgmask = fgbg.apply(frame)
    fgmask = cv2.morphologyEx(fgmask, cv2.MORPH_OPEN, kernel)

    cv2.imshow('frame',fgmask)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cv2.destroyAllWindows()
