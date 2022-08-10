import cv2
import numpy as np
roi = cv2.imread('color_A.jpg')#color a buscar 
hsv = cv2.cvtColor(roi,cv2.COLOR_BGR2HSV)
target = cv2.imread('rosasb.jpg')#imagen
hsvt = cv2.cvtColor(target,cv2.COLOR_BGR2HSV)
# calcula el histograma del objeto
roihist = cv2.calcHist([hsv],[0, 1], None, [180, 256], [0, 180, 0, 256] )
# normaliza el histograma y aplica la retroproyección
cv2.normalize(roihist,roihist,0,255,cv2.NORM_MINMAX)
dst = cv2.calcBackProject([hsvt],[0,1],roihist,[0,180,0,256],1)
# Ahora aplica la covolución con un disco
disc = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(6,6))
cv2.filter2D(dst,-1,disc,dst)
# Aplica un umbral y convierte la imagen en blanco y negro
ret,thresh = cv2.threshold(dst,70,255,0)
thresh = cv2.merge((thresh,thresh,thresh))
res = cv2.bitwise_and(target,thresh)
res = np.vstack((target,thresh,res))
cv2.imshow('res.jpg',res)
