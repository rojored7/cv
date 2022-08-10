import numpy as np
import cv2

#cargar imagen en escala de grises 
img = cv2.imread('rosasB.jpg',1)
#sin estecomando normalmente la bandera esta en cv2.WINDOW_AUTOSIZE
cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.imshow('image',img)

#se pone  & 0xFF siempre que sea maquina de 64 bits de resto no
k = cv2.waitKey(0) & 0xFF
if k == 27: # espera por esc para salir 
  cv2.destroyAllWindows() #Destruir las ventanas
elif k == ord('s'): #espera por s pasa guradr u salir
  cv2.imwrite('rosass.png',img)#guardar una imagen
  cv2.destroyAllWindows()   #destruir las ventanas
