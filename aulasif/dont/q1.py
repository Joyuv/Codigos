#region 1
tam = int(input('Insira o numero de linhas e colunas: '))
m = []


for x in range(tam):
    lin = ['_'] * tam
    m.append(lin)
#endregion

while True:

    print('\t\tMenu\n\n1 - Adicionar\n2 - Pesquisar\n3 - Exibir\n4 - Trocar\n5 - Sair')

    menu = int(input('Insira sua opção: '))

    if menu == 1:
        while True:
            nome = input('Insira o nome a ser inserido: ')
            pos_x = int(input('Insira a coluna: '))
            pos_y = int(input('Insira a linha: '))
            if pos_x > tam or pos_y > tam:
                print('Posição inexistente:')
            else:
                m[pos_x-1][pos_y-1] = nome.capitalize()
            
            menu2 = input('Quer Continuar? (s/n): ')

            if menu2.lower() == 'n':
                break
            else: pass
    
    if menu == 2:
        pesq = input('Insira um nome: ')

        if pesq.capitalize() in m:
            for x in range(len(m)):
                for y in range(len(m[x])):
                    