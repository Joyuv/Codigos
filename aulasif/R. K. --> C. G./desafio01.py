matriz = []

quant_l = int(input('insira a quantidade de linhas: '))
quant_c = int(input('insira a quantidade de colunas: '))

for x in range(0, quant_l):
    linha = []
    for y in range (0, quant_c):
        elemento = input(f'insira o elemento do item ({x+1}X{y+1})')
        linha.append(elemento)
    matriz.append(linha)

for x in matriz:
    print(x)