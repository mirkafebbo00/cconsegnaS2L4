import math

def media_mobile( lista, n):
    lista : list[float | int]
    n : int

    numeri = [1,2,3,4,5,6,7,8,9,10]
   

    print(media_mobile(numeri, n))

    medie =[]
    for i in range(len(lista)):
        finestra = lista[max(0, i - n +1): i + 1]
        medie.append(sum(finestra) / len(finestra))
        return medie