# OpenCV is an image and video processing library for all sort of image and video analysis.
import cv2
import numpy as np
import matplotlib.pyplot as plt
img = cv2.imread(r'C:\Users\UPES\Pictures\pic1.jpg', cv2.IMREAD_GRAYSCALE)
plt.imshow(img,cmap = 'gray' )
plt.plot([50,100],[80,100], '+')
plt.show()
