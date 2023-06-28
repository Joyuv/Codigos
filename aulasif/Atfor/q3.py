soma = 0
qt = 0
for x in range (1,51):

    num = int(input('insira um número: '))
    soma = soma + num
    qt += 1

    opc = input('Quer parar de inserir números? ((S) para parar/Qualquer tecla para continuar)')

    if opc == 'S':

        break
        
med = soma/qt
print(f'A média de seus números é {med}')