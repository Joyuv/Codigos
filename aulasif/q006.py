lista = []
while True:

    numero = int(input('insira um número a seguir (0 para parar): '))

    if numero == 0:
        break
    if numero != 0:
        lista.append(numero)

numerocomp = int(input('insira um número para comparar-mos com a lista: '))
estado = 0
for x in lista:

    if numerocomp == x:
        estado = 1
    
if estado == 0:
    print('O número não está na lista :(')
if estado == 1:
    print('O número está na lista :)')