import random

a1 = input('Insira o nome de quatro alunos. Nome do primeiro: ')
a2 = input('Segundo: ')
a3 = input('Terceiro: ')
a4 = input('Quarto: ')
lista = [a1, a2, a3, a4]

e = random.choice(lista)
print('O aluno(a) escolhido(a) foi {}'.format(e))