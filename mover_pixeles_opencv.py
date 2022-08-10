import cv2
import numpy as np
img = cv2.imread('rosasb.jpg')

#px = img[100,100]

# accessing only blue pixel
#blue = img[100,100,0]

#separar los canales bgr de una imagen muestra cada canal de imagen
b,g,r = cv2.split(img)
a = img[:,:,0]
b = img[:,:,1]
c = img[:,:,2]
#combinar 
img = cv2.merge((b,g,r))
#al cambiar el tercer valor en el arreglo 0,1,2 cambia el valor del pixel que se hacen 0 entre BGR
img[:,:,2] = 0
#mostrar imagen
cv2.imshow('imag',img)
cv2.imshow('imaa',a)
cv2.imshow('imab',b)
cv2.imshow('imac',c)
