nome = input('insira seu nome: ')
tam = len(nome)

lista = []
tupla = ()

for x in nome:
    lista.append(x)

tupla = list(tupla)
for x in nome:
    tupla.append(x)
tupla = tuple(tupla)

print(f'{tam}\n{type(tupla)}: {tupla}\n{type(lista)}: {lista}')