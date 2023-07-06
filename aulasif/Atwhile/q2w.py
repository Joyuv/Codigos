pessoar = 'Ninguém'
alturar = 0
while True:
    pessoa = input('Insira o nome da pessoa a seguir (digite N para parar de inserir dados): ')
    if pessoa == 'N':
        break
    altura = float(input('Insira a altura desta pessoa a seguir: '))
    if altura > alturar:
        alturar = altura
        pessoar = pessoa
if pessoar != 'Ninguém':
    print(f'A pessoa mais alta é {pessoar} com íncriveis {alturar}m de altura.')