inventario_tech = ["laptop","tarjeta de video","procesador","memoria RAM"]
print(inventario_tech)
inventario_tech.append("disco SSD")
print(inventario_tech)
inventario_tech.insert(2,"fuente de poder")
print(inventario_tech)
inventario_tech.extend(["gabinete","monitor 4K","teclado mecanio","mouse gamer"])
print(inventario_tech)
posicion = inventario_tech.index("monitor 4K")
print(posicion)
inventario_tech[3] = "memoria RAM DDR5"
print(inventario_tech)
equipo_depachado = inventario_tech.pop()

inventario_tech.remove("tarjeta de video")

print(equipo_depachado)

print(inventario_tech)

print("la cantidad total de componentes que quedan es ", len(inventario_tech) )
