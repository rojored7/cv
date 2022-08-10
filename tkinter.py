from tkinter import *
import tkinter as tk
import tkMessageBox

def helloCallBack():
   tkMessageBox.showinfo( "Hello Python", "Hello World")

label3.place(x=550,y=280)
label4=tk.Label(root,text="Temperratura")
label4.pack()
label4.place(x=450,y=200)
label5=tk.Label(root,text="Presion")
label5.pack()
label5.place(x=450,y=240)
label6=tk.Label(root,text="Humedad")
label6.pack()
label6.place(x=450,y=280)
label7=tk.Label(root,text="ºC")
label7.pack()
label7.place(x=750,y=200)
label8=tk.Label(root,text="hPa")
label8.pack()
label8.place(x=750,y=240)
label9=tk.Label(root,text="%")
label9.pack()
label9.place(x=750,y=280)

btn1 = Button(root, text = 'nano_on', command = helloCallBack, width=10, height=5)
btn1.place(x =  10, y = 10)
btn2 = Button(root, text = 'Directo', command = helloCallBack, width=10, height=5)
btn2.place(x = 150, y = 10)
btn3 = Button(root, text = 'Inverso', command = helloCallBack, width=10, height=5)
btn3.place(x = 290, y = 10)
btn4 = Button(root, text = 'Mitad', command = helloCallBack, width=10, height=5)
btn4.place(x = 440, y = 10)
btn5 = Button(root, text = 'Var', command = helloCallBack, width=10, height=5)
btn5.place(x = 580, y = 10)
btn6 = Button(root, text = 'txt', command = helloCallBack, width=10, height=5)
btn6.place(x = 150, y = 150)



slider1 = Scale(root,from_=1,to=500,orient = HORIZONTAL,resolution=1)
slider1.place(x=10,y=110)
d=slider1.get()
slider2 = Scale(root,from_=0.01,to=0.001,orient = HORIZONTAL,resolution=0.001)
slider2.place(x=10,y=150)
a=slider2.get()
