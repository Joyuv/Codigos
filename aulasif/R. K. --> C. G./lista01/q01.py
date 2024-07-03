impar = []
par = []

for x in range (0, 5):
    numero = int(input('insira um número: '))
    if numero % 2 == 0:
        print('o número é par.\n')
        par.append(numero)
    if numero % 2 == 1:
        print('o número é ímpar.\n')
        impar.append(numero)

print(f'Ímpar: {impar}\nPar: {par}')
