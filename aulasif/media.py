# Programa para calcular média

e = int(input('insira o número de notas para calcular a média 4/2'))

print('Programa que calcula média.')

if (e == 2):

    v1 = int(input('\n insira o primeiro valor: '))

    v2 = int(input('\n insira o segundo valor: '))

if (e == 4):

    v1 = int(input('\n insira o primeiro valor: '))

    v2 = int(input('\n insira o segundo valor: '))

    v3 = int(input('\n insira o terceiro valor: '))

    v4 = int(input('\n insira o quarto valor: '))


if (e == 2):

    m = (v1 + v2) / 2

if (e == 4):

    m = (v1 + v2 + v3 + v4) / 4

if (m >= 60):

    print('\na sua média é {} parabéns você passou '.format(m))

elif (m):

    print('sua média é {} que pena você não passou'.format(m))
