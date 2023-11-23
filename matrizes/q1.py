from random import randint as rand
matriz = []

linhas = int(input('insira a quantidade de linhas: '))
colunas = int(input('insira a quantidade de colunas que cada linha terá: '))

for x in range (linhas):
    for y in range(colunas):
        rando = rand(0,100000)
        if y == 0:
            linha = [rando]
        if y != 0:
            linha += [rando] 
    matriz.append(linha)

print(matriz)