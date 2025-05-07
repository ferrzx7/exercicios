def somar_notas (lista):
    total = 0 
    for i in lista:
        total += i
    media = total/len(lista)
    return media

nota = [7, 10, 8, 9]

print(somar_notas(nota))