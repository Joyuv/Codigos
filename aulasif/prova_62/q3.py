a = int(input('insira o valor de prateleiras: '))
b = int(input('insira o valor de livros que elas comportam: '))
bib = []
for x in range(a):
    bib.append([''] * b)
    
while True:
    print('Na biblioteca o teto é o limite, escolha a sua operação!\n1 - Pesquisar livro\n2 - Adicionar livro\n3 - Trocar livro\n4 - Imprimir estante\n5 - Sair')
    
    zezo = int(input('\nInsira sua opção a seguir: '))
    
    if zezo == 1:
        pesqs = 0
        pesq = input('Insira o nome do livro: ')
        for x in range(len(bib)):
            for y in range(len(bib[x])):
                ref = bib[x][y] 
                if ref.lower() == pesq.lower():
                    print(f'O livro {pesq} foi encontrado na prateleira {x+1} posição {y+1}')
                    pesqs = 1
        if pesqs == 0:
            print(f'O livro {pesq} não foi encontrado :(')

    if zezo == 2:
        livro = input('Insira o nome do livro a ser adicionado: ')
        prateleira = int(input('Insira a prateleira: '))
        pos = int(input('Insira a posição: '))

        if prateleira - 1 > a:
            print('Posições inválidas :(, voce será redirecionado ao menu!')
        elif pos - 1 > b:
            print('Posições inválidas :(, voce será redirecionado ao menu!')
        else:
            bib[prateleira - 1][pos - 1] = livro

    if zezo == 3:
        pesqs = 0
        pesq = input('Insira o nome do livro: ')
        for x in range(len(bib)):
            for y in range(len(bib[x])):
                ref = bib[x][y] 
                if ref.lower() == pesq.lower():
                    print(f'O livro {pesq} foi removido da prateleira {x+1} posição {y+1}')
                    bib[x][y] = ''
                    pesqs = 1
        if pesqs == 0:
            print(f'O livro {pesq} não foi encontrado :(')
    if zezo == 4:
        for x in range(0, len(bib)):
            print(f'Prateleira {x+1}: ', end = '')
            for y in range(0, len(bib[x])):
                if bib[x][y] != '':
                    print(f' {bib[x][y]} |', end = '')
                if bib[x][y] == '':
                    print(f' [Vazio] |', end = '')
            print('\n')
    if zezo == 5:
        print('Tenha um ótimo dia!')
        break