# importing OpenCV, time and Pandas library
import cv2, time
# importing datetime class from datetime library
from datetime import datetime
 
# Assigning our static_back to None
static_back = None 
 
# Capturing video
cam = cv2.VideoCapture(0)
 
# Infinite while loop to treat stack of image as video
while True:
    # Reading frame(image) from video
    check, frame = cam.read()
 
    # Converting color image to gray_scale image
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
 
    # Converting gray scale image to GaussianBlur 
    # so that change can be find easily
    gray = cv2.GaussianBlur(gray, (21, 21), 0)
 
    # In first iteration we assign the value 
    # of static_back to our first frame
    if static_back is None:
        static_back = gray
        continue
 
    # Difference between static background 
    # and current frame(which is GaussianBlur)
    diff_frame = cv2.absdiff(static_back, gray)
 
    # If change in between static background and
    # current frame is greater than 30 it will show white color(255)
    thresh_frame = cv2.threshold(diff_frame, 30, 255, cv2.THRESH_BINARY)[1]
    thresh_frame = cv2.dilate(thresh_frame, None, iterations = 2)
 
    # Finding contour of moving object
    (_, cnts, _) = cv2.findContours(thresh_frame.copy(), 
                       cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
 
    for contour in cnts:
        if cv2.contourArea(contour) < 10000:
            continue
        motion = 1
 
        (x, y, w, h) = cv2.boundingRect(contour)
        # making green rectangle arround the moving object
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)
 
 
    # Displaying image in gray_scale
    cv2.imshow("Gray Frame", gray)
 
    # Displaying the difference in currentframe to
    # the staticframe(very first_frame)
    cv2.imshow("Difference Frame", diff_frame)
 
    # Displaying the black and white image in which if
    # intencity difference greater than 30 it will appear white
    cv2.imshow("Threshold Frame", thresh_frame)
 
    # Displaying color frame with contour of motion of object
    cv2.imshow("Color Frame", frame)
 
    key = cv2.waitKey(1)
    # if q entered whole process will stop
    if key == ord('q'):
        # if something is movingthen it append the end time of movement
        if motion == 1:
            time.append(datetime.now())
        break
 

 
cam.release()
 
# Destroying all the windows
cv2.destroyAllWindows()
