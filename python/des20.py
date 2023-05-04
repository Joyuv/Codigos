import random

a1 = input('Grupo um: ')
a2 = input('Grupo dois: ')
a3 = input('Grupo três: ')
a4 = input('Grupo quatro: ')
lista = [a1, a2, a3, a4]

lf = random.shuffle(lista)

print('A sequencia de apresentação é {}'.format(lista))