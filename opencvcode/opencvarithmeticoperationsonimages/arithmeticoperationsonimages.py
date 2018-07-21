import cv2
import numpy as np

"""
#adding images
img = np.zeros((300,512,3), np.uint8)
x = np.uint8([250])
y = np.uint8([10])
while (1):
    cv2.imshow('image',img)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break

#blending images
#both images need to be of same size for this to work
img1 = cv2.imread('dragon.jpg')
img2 = cv2.imread('me_thunderleopard.JPG')
print(type(img1))
img1r = cv2.resize(img1, (200,200),interpolation=cv2.INTER_AREA)
img2r = cv2.resize(img2, (200,200),interpolation=cv2.INTER_AREA)
dst = cv2.addWeighted(img1r,0.3,img2r,0.7,0)
print(type(dst))
cv2.imshow('dst',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
"""
img1 = cv2.imread('dragon.jpg')
img2 = cv2.imread('opencv_logo.png')
img1 = cv2.resize(img1, (200,200),interpolation=cv2.INTER_AREA)
img2 = cv2.resize(img2, (200,200),interpolation=cv2.INTER_AREA)
rows,cols,channels = img2.shape
roi = img1[0:rows, 0:cols ]

img2gray = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(img2gray, 10, 255, cv2.THRESH_BINARY)
mask_inv = cv2.bitwise_not(mask)

# Now black-out the area of logo in ROI
img1_bg = cv2.bitwise_and(roi,roi,mask = mask_inv)

# Take only region of logo from logo image.
img2_fg = cv2.bitwise_and(img2,img2,mask = mask)

# Put logo in ROI and modify the main image
dst = cv2.add(img1_bg,img2_fg)
img1[0:rows, 0:cols ] = dst

cv2.imshow('res',img1)
cv2.waitKey(0)
cv2.destroyAllWindows()
