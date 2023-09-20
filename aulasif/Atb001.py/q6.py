nomes = ['bacalhau', 'peixe', 'farelo', 'banana', 'malvado', 'mecânico',
'amarelo', 'farelo', 'farelo', 'amendoim', 'peixe']

nomes.sort()

cont = 0
for nome in nomes:

    if nome == 'bacalhau':
        cont += 1

print(f'A lista contém {cont} instâncias da palavra bacalhau\n')

cont = 0

tam = len(nomes)

while cont < tam:

    if nomes[cont] == 'farelo':
        nomes.pop(cont)
        tam -= 1
        cont -= 1
    
    cont += 1

for x in range (3, 0, -1):

    pala = input(f'Insira uma palavra ({x} palavras restando): ')
    print('\n')
    nomes.append(pala)

nomes.sort()
nomes.reverse()

cont = 0
for nomades in nomes:

    print(f'{cont} --> {nomades}\n')
    cont += 1

print(nomes)