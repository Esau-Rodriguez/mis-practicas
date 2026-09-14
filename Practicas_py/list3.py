frutas = ["manzana","guayaba","uva"]

#ACTUALIZAR
frutas[1]="pera"

#INSERTAR
frutas.append("sandia")
#INSERTAR VARIOS
frutas.extend(["mango","melon"])

#ELIMINAR
retirado = frutas.pop(2)
#ELIMINAR ULTIMO ELEMENTO
ultimo = frutas.pop()

#BUSCA EL VALOR EXACTO Y ELIMINA LA PRIMERA APARICION
frutas.remove("sandia")

#del Utiliza palabra clave para borrar una casilñla directamente 
del frutas[0]

posicion = frutas.index("pera")

print(frutas)
print(posicion)