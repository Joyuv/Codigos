vzs = int(input('inira quantas vezes deseja usar o programa: '))

for i in range(vzs):

    numero = int(input('digite um numero a seguir: '))

    if numero < 0 or numero == 0:

        break

    for x in range(1,11):

        print(f'{numero} * {x} = {numero*x}')