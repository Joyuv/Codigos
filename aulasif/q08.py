pnome = input('insira seu primeiro nome a seguir: ')
list1 = []
for x in pnome:
    list1.append(x)

snome = input('insira o seu segundo nome a seguir: ')
list2 = []
for x in snome:
    list2.append(x)
print(f'O seu primeiro nome possui {len(list1)} letras o segundo tem {len(list2)} e o seu nome completo é {pnome} {snome}')