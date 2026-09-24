import matplotlib.pyplot as plt
#Funcion now()

from datetime import datetime
ahora = datetime.now()
print(ahora) 

#Funcion strftime()
texto_fecha = ahora.strftime("%d/%m/%Y a las %H:%M")
print(texto_fecha) 

#Funcion (f-strings)
nombre = "Carlos"
edad = 25
mensaje = f"Hola, me llamo {nombre} y el próximo año tendré {edad + 1} años."
print(mensaje) 
nombre = "Carlos"
edad = 25
# Uniendo texto y variables fácilmente
mensaje = f"Hola, me llamo {nombre} y el próximo año tendré {edad + 1} años."
print(mensaje) 

#Librebria matplotlib
meses = ['Ene', 'Feb', 'Mar']
ventas = [100, 150, 120]

plt.plot(meses, ventas)
plt.title("Ventas Trimestrales")
plt.show() # Abre una ventana con el gráfico generado

