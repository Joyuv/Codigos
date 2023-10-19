pnome = input('insira seu primeiro nome a seguir: ')
list1 = []
for x in pnome:
    list1.append(x)

snome = input('insira o seu segundo nome a seguir: ')
list2 = []
for x in snome:
    list2.append(x)

def nome_completo(l1,l2):
    nomecompleto = ''
    for x in l1:
        nomecompleto = nomecompleto + x
    nomecompleto += ' '
    for x in l2:
        nomecompleto = nomecompleto + x
    return nomecompleto
print(f'O seu primeiro nome possui {len(list1)} letras o segundo tem {len(list2)} e o seu nome completo é {nome_completo(list1, list2)}')