nomes = ['bruno', 'josé', 'natheus', 'abraão', 'abraão']
pos = []
nome = input('insira um nome, o procuraremos na lista: ')
vezes = 0
for x in range (0,len(nomes)):
    if nomes[x] == nome and vezes > 0:
        vezes += 1, pos.append(x)
        print(f'O nome {nome} foi encontrado mais de uma vez, mais exatamente {vezes} vezes nas posições {pos}') 
    elif nomes[x] == nome:
        print(f'O nome {nome} foi encontrado na posição [{x}].')
        vezes += 1, pos.append(x) 