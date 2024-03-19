prim = 0
div = 0
while prim < 3:
    numero = int(input('insira o número a seguir:'))

    if numero == 1:
        print('É primo.')
        prim += 1
    else:
        for x in range (numero, 1, -1):
            if numero % x == 0:
                div += 1
        if div > 1:
            print('Não é primo.')
        else:
            print ('É primo.')
            prim += 1
    div = 0
    