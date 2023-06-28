soma = 0

for x in range (1,6):

    sr = soma
    nota = int(input('insira a nota: '))

    soma = soma + nota

med  = soma / x

print(f'sua média é {med}, se você passou ou não de ano eu sou incapaz de dizer :(')