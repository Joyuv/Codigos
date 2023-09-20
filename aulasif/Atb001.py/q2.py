numeros = []
numero = 1
soma = 0
cont = 0

while numero != 0:

    numero = int(input('insira um número a seguir (Digite um 0 para parar): '))
    numeros.append(numero)

for numrs in numeros:

    if numrs < 0:
        break

    soma += numrs
    cont += 1

print(f'A média de tudo que você me providenciou até o primeiro número negativo (ou fim dos números em\ncaso de não ter me fornecido algum negativo) é {soma / cont}')

