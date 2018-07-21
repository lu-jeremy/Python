import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('j.jpg',0)

# Initiate FAST object with default values
fast = cv2.FastFeatureDetector_create()

# find and draw the keypoints
color=(255,0,0)
kp = fast.detect(img,None)
img2 = cv2.drawKeypoints(img, kp, None, color)

# Print all default params
print("Threshold: ", fast.getThreshold)
print("nonmaxSuppression: ", fast.getNonmaxSuppression())
print("neighborhood: ", fast.getType())
print("Total Keypoints with nonmaxSuppression: ", len(kp))

cv2.imshow('fast_true.png',img2)

# Disable nonmaxSuppression
fast.setNonmaxSuppression(0)
kp = fast.detect(img,None)

print("Total Keypoints without nonmaxSuppression: ", len(kp))

img3 = cv2.drawKeypoints(img, kp, None,color)

cv2.imshow('fast_false.png',img3)
