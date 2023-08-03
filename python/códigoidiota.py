import random

lista = []

for x in range (0,2):
    nome = input('insira um nome a seguir: ')
    lista.append(nome)

nome1 = lista[0]
nome2 = lista[1]
porcentagem = random.randrange(90, 100)

print(f'{nome1} e {nome2} combinam {porcentagem}%')