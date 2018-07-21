import cv2
import numpy as np
from matplotlib import pyplot as plt
"""
#find plot, analyze histograms
img = cv2.imread('c1.png',0)
#hist = cv2.calcHist([img],[0],None,[256],[0,256])
plt.hist(img.ravel(),100,[0,256])
plt.show()
"""
"""
img = cv2.imread('c1.png')
color = ('b','g','r')
for i,col in enumerate(color):
    histr = cv2.calcHist([img],[i],None,[256],[0,256])
    plt.plot(histr,color = col)
    plt.xlim([0,256])
plt.show()
"""
#histogram equalization

img = cv2.imread('c1.png',0)
equ = cv2.equalizeHist(img)
res = np.hstack((img,equ)) #stacking images side-by-side
cv2.imwrite('res.png',res)
