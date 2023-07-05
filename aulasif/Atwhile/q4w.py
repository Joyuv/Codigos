soma = 0
qt = 0
while True:
    num = int(input('Insira um número a seguir: '))
    soma = soma + num
    qt += 1
    if soma > 2000:
        break
    if qt >= 15:
        break
print(f'A soma de tudo é {soma}.')