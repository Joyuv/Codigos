lista = []
nome = 'Vazio'
while nome != 'sair':
    nome = input('insira um nome ')
    if nome != 'sair':
        lista.append(nome)
print(lista)