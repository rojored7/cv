import cv2
#Carga la imagen
img = cv2.imread('rosas.jpg')
#Convierte la imagen a escala de grises
imgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret,thresh = cv2.threshold(imgray,127,255,0)
#Determina los contornos
contours, hierarchy = cv2.findContours(thresh,1,2)
cnt = contours[0]
#Determina los defectos de convexidad
envoltura = cv2.convexHull(cnt,returnPoints = False)
defectos = cv2.convexityDefects(cnt,envoltura)
#Dibuja la envoltura convexa y los defectos de convexidad
for k in range(defectos.shape[0]):
    i,f,l,d = defectos[k,0]
    inicio= tuple(cnt[i][0])
    fin= tuple(cnt[f][0])
    lejos = tuple(cnt[l][0])
    cv2.line(img,inicio,fin,[0,255,255],2)
    cv2.circle(img,lejos,5,[0,0,255],-1)
#Muestra la imagen final
cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
#Guarda la imagen
cv2.imwrite('def_convexidad.tif',img)
