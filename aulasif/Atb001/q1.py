valores = []
for x in range (0,5):

    valor = int(input('insira um valor numérico: '))
    valores.append(valor)

negativos = 0
for valorl in valores:

    if valorl < 0:

        negativos += 1

        if negativos >= 2:
        
            print(f'\nO valor ({valorl}) é negativo, com este contabilizam {negativos} valores negativos.')
        if negativos <= 1:

            print(f'\nO valor ({valorl}) é negativo, com este contabiliza {negativos} valor negativo.')

if negativos <= 1:
            
    print(f'\nAo todo foi encontrado {negativos} valor negativo.')
if negativos >= 2:
     
    print(f'\nAo todo foram encontrados {negativos} valores negativos.')