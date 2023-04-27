n1 = int(input('insira o valor da primeira nota'))
n2 = int(input('insira o valor da segunda nota'))
n3 = int(input('insira o valor da tercaira nota'))
n4 = int(input('insira o valor da quarta nota'))

#calculo

nf = (n1 * (10/100)) + (n2 * (50/100)) + (n3 * (15/100)) + (n4 * (25/100))

print('o seu valor final é {}'.format(nf))