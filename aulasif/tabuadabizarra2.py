lista = [10, 25, 9, 85, 56, 8, 6, 7, 13]
resultado = []
for x in range(0, len(lista)):
    if lista[x] % 2 != 0:
        resultado.append(lista[x]*10)
print(resultado)