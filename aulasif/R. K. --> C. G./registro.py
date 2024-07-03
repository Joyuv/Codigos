agenda = {}

for x in range (0,2):
    nome = input('insira o nome do contato: ')
    numero = int(input('insira o número do contato: '))
    agenda.update({numero: nome})

for x in agenda:
    print(f'Número: {x} Nome: {agenda[x]}')