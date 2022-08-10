import cv2
import numpy as np
from matplotlib import pyplot as plt
img = cv2.imread('clavelR1.jpg')
color = ('b','g','r')
cv2.imshow('im',img)    
for i,col in enumerate(color):
    histr = cv2.calcHist([img],[i],None,[256],[0,256])
    plt.plot(histr,color = col)
    plt.xlim([0,256])
plt.show()

