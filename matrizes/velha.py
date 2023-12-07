














        print()

    pos_l = int(input('Posição da linha: '))
    pos_c = int(input('posição da coluna: '))

    if jogador == 'X':
        tabuleiro[pos_l][pos_c] = 'X'
        jogador = 'O'
    if jogador == 'O':
        tabuleiro[pos_c]{pos_c} = 'O'
        jogador = 'X'