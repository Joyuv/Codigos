reg = {}
rep = []
apr = []
nome = ''

while nome.lower() != 'pare':
    nome = input('Insira o nome do aluno: ')
    if nome.lower() == 'pare':
        break
    nota = float(input('Insira a nota do aluno: '))
    if nota >= 60.0:
        apr.append(nome)
    else:
        rep.append(nome)

reg.update({'reprovado': rep})
reg.update({'aprovado': apr})

for x in reg:
    print(f'''---------------{x.upper()}{'-'*(24 - len(x))}''')
    for z in reg[x]:
        print(f'{z.capitalize()}')
print(f'''------------------FIM{'-'*(24 - 6)}''')
