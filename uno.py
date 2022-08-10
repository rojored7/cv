import matplotlib.pyplot as plt
import numpy as np # Importamos numpy como el alias np
a = np.linspace(0,20,50)
b= np.sin(a)
c=plt.plot(a, b, 'c-3', linewidth = 2)
c=plt.plot(a+0.2, b-1, 'r-o', linewidth = 2)
plt.xlabel("Tiempo (s)", fontsize = 20)
plt.ylabel(r"$y (\mu m)$", fontsize = 24, color = 'blue')
plt.text(5, 7, "Más texto", fontsize = 12)
plt.title("velocidad (m/s)", fontsize = 20)
plt.legend( ('Etiqueta1', 'Etiqueta2', 'Etiqueta3'), loc = 'upper left')
plt.grid(True)
plt.savefig('figura3.png', dpi = 300) #guarda la gráfica con 300dpi (puntos por pulgada)
plt.show()