def bubbleSort(lista):
    for numero in (len(lista)-1,0,-1):
        for i in range(numero):
            if lista[i] > lista[i+1]:
                temp = lista[i]
                lista[i] = lista[i+1]
                lista[i+1]=temp


lista = [10,30,25,2,11,4,56,33]
bubbleSort(lista)
print(lista)