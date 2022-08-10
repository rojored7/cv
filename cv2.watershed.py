import numpy as np
import cv2
from matplotlib import pyplot as plt
img = cv2.imread('clavel.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(gray,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)

# Eliminación del ruido
kernel = np.ones((3,3),np.uint8)
opening = cv2.morphologyEx(thresh,cv2.MORPH_OPEN,kernel, iterations = 2)
# Encuentra el área del fondo
sure_bg = cv2.dilate(opening,kernel,iterations=3)
# Encuentra el área del primer
dist_transform = cv2.distanceTransform(opening,cv2.DIST_L2,5)
ret, sure_fg = cv2.threshold(dist_transform,0.7*dist_transform.max(),255,0)
# Encuentra la región desconocida (bordes)
sure_fg = np.uint8(sure_fg)
unknown = cv2.subtract(sure_bg,sure_fg)
# Etiquetado
ret, markers = cv2.connectedComponents(sure_fg)
# Adiciona 1 a todas las etiquetas para asegurra que el fondo sea 1 en lugar de cero
markers = markers+1
# Ahora se marca la región desconocida con ceros
markers[unknown==255] = 0
cv2.imshow('im',markers)
cv2.imshow('ori',img)
