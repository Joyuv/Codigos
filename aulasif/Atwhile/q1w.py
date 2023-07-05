soma = 0
while True:
    num = int(input('Insira um número a seguir (digite 0 para parar o programa): '))
    if (num % 2) != 0:
        soma = soma + num
    if (num == 0):
        print(f'a soma total dos números ímpares que você me deu é {soma}')
        break