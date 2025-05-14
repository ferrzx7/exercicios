def somar_notas (lista):
    total = 0 
    for i in lista:
        total += i
    media = total/len(lista)
    return media

