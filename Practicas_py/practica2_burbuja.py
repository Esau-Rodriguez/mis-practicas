calificaciones = [8,7,9,10,6,7,9,8,7,10,9,10,8,10,7]
n = len(calificaciones)
swapped = True

#Ordenamiento ascendente
while  swapped:
    swapped = False
    for i in range(n-1):
        if calificaciones[i]>calificaciones[i+1]:
            calificaciones[i],calificaciones[i+1]=calificaciones[i+1],calificaciones[i]
            swapped = True
print("Orden ascendente: ",calificaciones)

#Ordenamiento descendente
while  swapped:
    swapped = False
    for i in range(n-1):
        if calificaciones[i]<calificaciones[i+1]:
            calificaciones[i],calificaciones[i+1]=calificaciones[i+1],calificaciones[i]
            swapped = True
print("Orden descendente: ",calificaciones)

#Descendente con metodo tradicional
for i in range(len(calificaciones)):
    for x in range(len(calificaciones)-1):
        if calificaciones[x]<calificaciones[x+1]:
            aux = calificaciones[x]
            calificaciones[x]=calificaciones[x+1]
            calificaciones[x+1]=aux
print("Orden descendente: ", calificaciones)