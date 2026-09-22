lista = [5, 2, 4, 6, 1, 3]

for i in range(1,len(lista)):
    actual = lista[i]
    j = i - 1
    while j >= 0 and lista[j] > actual:
        lista[j + 1] = lista[j]
        j -= 1
    lista[j + 1] = actual
    print(lista)

print("Lista ordenada:", lista)