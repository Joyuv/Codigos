soma = 0
while True:
    num = int(input('Insira um número a seguir (o número 0 é o critério de parada): '))
    if (num % 5) == 0:
        soma = num + soma
    if (num == 0):
        break
print(f'Seu valor final é {soma}.')