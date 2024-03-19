lista = []

while True:
    numero = int(input('insira o número: '))

    if numero == 0:
        lista.append(numero)
        lista.sort()
        break
    if numero in lista:
        pass
    else:
        lista.append(numero)
        lista.sort()
        print (lista)


print(lista)