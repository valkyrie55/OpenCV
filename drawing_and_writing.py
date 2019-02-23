# drawing and writing on image
import cv2
import numpy as np
import matplotlib.pyplot as plt
img = cv2.imread(r'C:\Users\UPES\Pictures\pic1.jpg', cv2.IMREAD_COLOR)
# for line
cv2.line(img, (0,0), (50,50),(0,255,0),5)
#for rectangle
cv2.rectangle(img,(50,700),(670,40),(255,255,0), 8)
#for circle
cv2.circle(img,(600,345),35,(0,0,255),-1)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
