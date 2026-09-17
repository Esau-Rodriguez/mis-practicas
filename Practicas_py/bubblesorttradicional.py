#Ordenamiento con bubble sort metodo tradicional
lista=[12,10,8,0,52,0]
print("Lista original",lista)
for i in range(len(lista)):
    for x in range(len(lista)-1):
        if lista[x] > lista[x+1]:
            aux = lista[x]
            lista[x] = lista[x+1]
            lista[x+1] = aux
            print(lista)
print("Lista ordenada ",lista)

