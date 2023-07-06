maiorv = 0
menorv = 1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
for a in range (0,10):
    valor = int(input('insira o valor: '))
    if valor > maiorv:
        maiorv = valor
    elif valor < menorv:
        menorv = valor
print(f'O maior valor é {maiorv}\nO menor é {menorv}.')