#Tabela de erros: 
#001A - Não inseriu oque se pedia ou não seguiu alguma regra previamente estabelecida.

a = []

while True:

    tam = int(input('Insira o tamanho da matriz (Ímpar): '))

    if tam % 2 == 0:
        print('Tamanho inválido, (Código do erro= 001A).')
    else:
        break

def print_m(matriz):
    for x in range(len(matriz)):
        for y in range(len(matriz[x])):
            print(matriz[x][y], end = '')
        print('')
    print('\n')

for x in range(tam):
    linha = ['_'] * tam

    a.append(linha)

print_m(a)

for x in range (len(a)):
    a [x][x] = 1

print_m(a)

for x in range (len(a)):
    for y in range (len(a[x])):
        if a[x][y] != '_':
            pass
        else:
            a[x][y] = 'A'

print_m(a)

a[(tam//2)][(tam//2)] = 'X'

print_m(a)
