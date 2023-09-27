lista1 = []
listap = []
listai = []
soma = 0

for x in range(0,6):

    numrs = int(input('insira uns numeros a seguir: '))
    lista1.append(numrs)

for x in lista1:

    if x % 2 == 0:

        listap.append(x)

        soma += x
    
    if x % 2 != 0:

        listai.append(x)
    
print(f'Os números pares são ({listap}) a soma de todos é ({soma}).\nOs números impares são ({listai}) a quantidade é ({len(listai)}).')
