import numpy as np
import cv2
import tkinter

#lectura imagen 0 BW/1 Color
imgc = cv2.imread('clavelR1.jpg')
img = cv2.imread('clavelR1.jpg', 0)
#separar los canales bgr de una imagen muestra cada canal de imagen
b,g,r = cv2.split(imgc)
c = imgc[:,:,2]

#binarizacion
#ret,thresh1 = cv2.threshold(img,252,255,cv2.THRESH_BINARY)#funciona con rosas_r1
ret,thresh1 = cv2.threshold(c,210,250,cv2.THRESH_BINARY)#funciona con rosasb

#thresh1 = cv2.adaptiveThreshold(c,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
# cv2.THRESH_BINARY,5,3)
#segmentacion y dilatacion
kernel = np.ones((2,2),np.uint16)
kernel1 = np.ones((1,1),np.uint16)
erosion = cv2.erode(thresh1,kernel,iterations =2)
dilatacion = cv2.dilate(erosion,kernel,iterations = 9)
#cierre
apertura = cv2.morphologyEx(dilatacion, cv2.MORPH_OPEN, kernel1)
#bordes con filtro canny
bordes =cv2.Canny(apertura,100,255)
bordes2 =cv2.Canny(apertura,150,210)

#contornos

ctns, _ = cv2.findContours(bordes, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(imgc, ctns, -2, (255,0,0), 2)

#calculo de diametro de los elementos 

x=len(ctns)
i=0
for i in range(x):
    cnt = ctns[i]
    (x,y),radius = cv2.minEnclosingCircle(cnt)
    center = (int(x),int(y))
    radius = int(radius)
    nueva = cv2.circle(imgc,center,radius,(0,255,0),2)
    cv2.imshow('circle', nueva)

##                 
#cv2.imshow('circle', nueva)
#mostrarar
#cv2.imshow('image', img)
#cv2.imshow('imagec', c)
#cv2.imshow('imac',c)
#cv2.imshow('erosion', erosion)
#cv2.imshow('dilatacion', dilatacion)
#cv2.imshow('bordes2', bordes2)
#cv2.imshow('apertura', apertura)
cv2.imshow('bordes', bordes)
#cv2.imshow('umbra', thresh1)
#print('Número de rosas: ', len(ctns))

cv2.waitKey(0)
cv2.destroyAllWindows()
