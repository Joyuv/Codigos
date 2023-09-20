numero = 1
numeros = []
soma = 0
cont = 0

while numero != 0:

    numero = int(input("Digite um número: "))
    if numero != 0:
        numeros.append(numero)

for x in numeros:

    if x % 2 == 0:
        soma += x
        cont += 1

print(numeros)
print(f'A média de todos os números pares da lista é {soma / cont}')