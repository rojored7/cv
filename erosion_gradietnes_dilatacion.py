import cv2
import numpy as np
from matplotlib import pyplot as plt
img = cv2.imread('rosasb.jpg',1)
kernel = np.ones((7,7),np.uint8)
erosion = cv2.erode(img,kernel,iterations = 1)
dilatacion = cv2.dilate(img,kernel,iterations = 1)
apertura = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
cierre = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
gradiente = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)
cv2.imshow('ima',img)
#hemos creado manualmente elementos estructurantes (kernels) de forma rectangular (utilizando np.ones()). Sin embargo, en
#algunos casos, es necesario crear núcleos elípticos / circulares.
#Para este propósito, OpenCV tiene la función cv2.getStructuringElement().
plt.subplot(431),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(432),plt.imshow(kernel),plt.title('kernel')
plt.xticks([]), plt.yticks([])
plt.subplot(433),plt.imshow(erosion),plt.title('erosion')
plt.xticks([]), plt.yticks([])
plt.subplot(434),plt.imshow(dilatacion),plt.title('dilatacion')
plt.xticks([]), plt.yticks([])
plt.subplot(435),plt.imshow(apertura),plt.title('apertura')
plt.xticks([]), plt.yticks([])
plt.subplot(436),plt.imshow(cierre),plt.title('cierre')
plt.xticks([]), plt.yticks([])
plt.subplot(437),plt.imshow(gradiente),plt.title('gradiente')
plt.xticks([]), plt.yticks([])


plt.show()
