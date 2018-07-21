import cv2
import time

"""
Assignments

put a rectangle around moving object

"""
cap = cv2.VideoCapture(0)

ret,frame = cap.read()

ret,frame1 = cap.read()

ret,frame2 = cap.read()
while(True):
    ret, frame = cap.read()
    ret,frame1 = cap.read()
    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray1 = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)
    ret,gray2 = cv2.threshold (gray2, 127,255,cv2.THRESH_BINARY);

    for height in range(720):
        for width in range(1280):
            if gray1[height][width]-gray[height][width] >= 20:
                gray2[height][width] = gray1[height][width]-gray[height][width]
            else:
                gray2[height][width] = 0
    

    # Display the resulting frame
    """
    cv2.imshow('frame',gray)

    cv2.imshow('frame1',gray1)
    """
    cv2.imshow('frame2',gray2)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()

