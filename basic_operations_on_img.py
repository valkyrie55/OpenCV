#basic image operations
import cv2
import numpy as n
img1 = cv2.imread(r'C:\Users\UPES\Pictures\sentdex1.png')
img2 = cv2.imread(r'C:\Users\UPES\Pictures\sentdex2.png')
#simple addition
addn = img1+ img2
cv2.imshow('resulting image 1',addn)
#to avoid the messy addition
a = cv2.add(img1, img2)
cv2.imshow('resulting image 2',a)
#we can give different weights to immages
weight = cv2.addWeighted(img1, 0.6,img2, 0.4,0)  #gamma(measurement of light) =0
cv2.imshow('resulted image', weight)
cv2.waitKey(0)
cv2.destroyAllWindows()
