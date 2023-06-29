soma = 0
qt = 0
for x in range (1,51):

    num = int(input('insira um número: '))

    if num >=0:
            
        soma = soma + num
        qt += 1

    if num < 0:

        break
        
med = soma/qt
print(f'A média de seus números é {med }')