# import the necessary packages
from tkinter import *
from PIL import Image
from PIL import ImageTk
from tkinter import filedialog
import cv2
import numpy as np

def hola():
    print("Hola mundo!")

def abrir():
   global panelA, panelB
   
   ruta=filedialog.askdirectory()
   path=filedialog.askopenfilename()
   
   if len(path)>0:
       imgc = cv2.imread(path,1)
       image = cv2.imread(path,1)
       b,g,r = cv2.split(imgc)
       c = imgc[:,:,2]
       ret,thresh1 = cv2.threshold(c,210,250,cv2.THRESH_BINARY)
       kernel = np.ones((2,2),np.uint16)
       kernel1 = np.ones((1,1),np.uint16)
       erosion = cv2.erode(thresh1,kernel,iterations =2)
       dilatacion = cv2.dilate(erosion,kernel,iterations = 9)
       apertura = cv2.morphologyEx(dilatacion, cv2.MORPH_OPEN, kernel1)
       bordes =cv2.Canny(apertura,100,255)
       ctns, _ = cv2.findContours(bordes, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
       cv2.drawContours(imgc, ctns, -2, (255,0,0), 2)
       x=len(ctns)
       i=0
       for i in range(x):
           cnt = ctns[i]
           (x,y),radius = cv2.minEnclosingCircle(cnt)
           center = (int(x),int(y))
           radius = int(radius)
           nueva = cv2.circle(imgc,center,radius,(0,255,0),2)
       image = Image.fromarray(c)
       image = ImageTk.PhotoImage(c)

   if panelA is None or panelB is None:
       panelA = Label(image=image)
       panelA.image = image
       panelA.pack(side="left", padx=10, pady=10)

   
root = Tk()
root.title('CONTEO DE FLOR')
root.geometry('1500x1000')

panelA = None
panelB = None

# Enlezamos la función a la acción del botón
btn1 = Button(root, text = 'busquela', command = abrir, width=10, height=5)
btn1.place(x =  10, y = 10)

root.update()
root.mainloop() 
