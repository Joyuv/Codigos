import random

a1 = input('Insira o nome de quatro alunos. Nome do primeiro: ')
a2 = input('Segundo: ')
a3 = input('Terceiro: ')
a4 = input('Quarto: ')

e = random.randint(1, 4)

if(e == 1):print('O aluno(a) escolhido(a) foi {}'.format(a1))
if(e == 2):print('O aluno(a) escolhido(a) foi {}'.format(a2))
if(e == 3):print('O aluno(a) escolhido(a) foi {}'.format(a3))
if(e == 4):print('O aluno(a) escolhido(a) foi {}'.format(a4))