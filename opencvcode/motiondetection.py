import cv2
import time

"""
Assignments

put a rectangle around moving object

"""
cap = cv2.VideoCapture(0)

ret,frame = cap.read()
frame = cv2.resize(frame,None,fx=0.25, fy=0.25, interpolation = cv2.INTER_CUBIC)
ret,frame1 = cap.read()
frame1 = cv2.resize(frame1,None,fx=0.25, fy=0.25, interpolation = cv2.INTER_CUBIC)
ret,frame2 = cap.read()
frame2 = cv2.resize(frame2,None,fx=0.25, fy=0.25, interpolation = cv2.INTER_CUBIC)
while(True):
    ret, frame = cap.read()
    ret,frame1 = cap.read()
    
    frame = cv2.resize(frame,None,fx=0.25, fy=0.25, interpolation = cv2.INTER_CUBIC)

    frame1 = cv2.resize(frame1,None,fx=0.25, fy=0.25, interpolation = cv2.INTER_CUBIC)

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    ret, binary = cv2.threshold(gray,127,255,cv2.THRESH_BINARY)
    gray1 = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
    ret, binary1 = cv2.threshold(gray1,127,255,cv2.THRESH_BINARY)
    
    gray2 = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)
    ret,binary2 = cv2.threshold(gray2, 127,255,cv2.THRESH_BINARY)


    for height in range(180):
        for width in range(320):
            if binary1[height][width] != binary[height][width]:
                binary2[height][width] = 1
            else:
                binary2[height][width] = 0
                
    
    image, contours, hierarchy = cv2.findContours(binary,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

    cv2.drawContours(binary, contours, -1, (0,255,0), 3)
    
    # Display the resulting frame
    
    cv2.imshow('frame',binary)

    cv2.imshow('frame1',binary1)
    
    cv2.imshow('frame2',binary2)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()

