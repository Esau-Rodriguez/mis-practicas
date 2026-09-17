#Ordenamiento de listas con bubble sort 
lista=[12,10,8,0,52,0]
n = len(lista)
swapped = True
while swapped:
    swapped = False
    for i in range(n-1):
        if lista[i]>lista[i+1]:
            lista[i],lista[i+1]= lista[i+1],lista[i]
            swapped=True
            print("Lista ordenada ",lista)
print("Lista ordenada ",lista)