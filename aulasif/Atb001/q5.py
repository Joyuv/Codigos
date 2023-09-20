lista = [10, 12, 23, 34, 45, 56, 67, 8, 9, 10, 11, 12, 13, 14, 15,
16, 17, 18, 19, 20]
numero = 0

for x in lista:

    if x % 2 == 0:
        numero += x
    if x % 2 != 0:
        numero -= x

print(f'O valor final após algums calculos é de {numero}')