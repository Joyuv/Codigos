arq = open('/home/giva/Codigos/aulasif/R. K./arquivos/agenda/agenda.txt', 'a')

while True:
    nome = input('insira o nome do cidadão (ou "pare"): ')
    if nome == 'pare':
        break
    numero = input(f'insira o numero de {nome}: ')
    arq.write(f'{nome} : {numero}')

arq.close()