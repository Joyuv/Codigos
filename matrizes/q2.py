from random import randint as rand
matriz = []

linhas = (rand(1,10))
colunas = (rand(1,10))

for x in range (linhas):
    for y in range(colunas):
        rando = rand(0,100)
        if y == 0:
            linha = [rando]
        if y != 0:
            linha += [rando] 
    matriz.append(linha)

print(matriz)

cont = 0
for x in range(len(matriz)):
    for y in matriz[x]:
        cont += 1

print(f'\nExistem {cont} elementos na lista acima.')