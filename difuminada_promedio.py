import cv2
import numpy as np
from matplotlib import pyplot as plt
img = cv2.imread('rosasb.jpg')
blur = cv2.blur(img,(3,3))#filtro de caja normalizado
#Si no desea utilizar un filtro de caja normalizado, utilice cv2.boxFilter() y pase el
#argumento normalize = False a la función.
blurg = cv2.GaussianBlur(img,(5,5),0)# filtro gaussiano ruido gaussiano
#median = cv2.medianBlur(img,5)#filtro de mediana para quitar ruido pequeño

plt.subplot(221),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(222),plt.imshow(blur),plt.title('Difuminada')
plt.xticks([]), plt.yticks([])
plt.subplot(223),plt.imshow(blurg),plt.title('Difuminadag')
plt.xticks([]), plt.yticks([])


plt.show()
