import numpy as np
import cv2
img = cv2.imread('rosasb.png',0)
# Crea un objeto CLAHE (los argumentos son opcionales).
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
cl1 = clahe.apply(img)
cv2.imshow('clahea',cl1)
