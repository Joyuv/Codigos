lin = int(input('Insira a quantidade de linhas que a matriz terá: '))
col = int(input('Insira a quantidade de colunas que a matriz terá: '))

m = []

for x in range(lin):
    linha = ['_'] * col
    m.append(linha)

while True:

    print('\t\tMENU\n1 - Adicionar elemento\n2 - Exibir a matriz\n3 - Média de números divisiveis por 3\n4 - Fechar\n')

    opc = int(input('Insira: '))

    if opc == 1:
        while True:
            pos_x = int(input('Insira a linha: '))
            pos_y = int(input('Insira a coluna: '))
            elm = int(input('Insira o elemento (Numérico) a ser adicionado: '))
            
            if pos_x > lin or pos_y > col:
                print('Posições inválidas tente novamente.')
            else:
                break

        m[pos_x-1][pos_y-1] = elm

    if opc == 2:
        for x in range(0, len(m)):
            for y in range(0, len(m[x])):
                print(m[x][y], end = '')
            print('')
        print('')
    if opc == 3:
        soma = 0
        cont = 0
        for x in range(len(m)):
            for y in range(len(m[x])):
                if m[x][y] != '_':
                    if m[x][y] % 3 == 0:
                        soma += m[x][y]
                        cont += 1
                else:
                    pass
                
        print(f'A média dos números divisiveis por (3) é: {soma/cont}')

    if opc == 4:
        break