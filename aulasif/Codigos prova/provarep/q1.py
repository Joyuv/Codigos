list1 = []
list2 = []
list3 = []
qnt = int(input('insira o número de clientes: '))

for x in range (0, qnt):

    nmr = int(input(f'Insira o número do cliente {x + 1}: '))
    ida = int(input(f'Insira a idade do cliente {x + 1}: '))
    cid = input(f'insira a cidade do cliente {x + 1}: ')
    print('\n')

    list1.append(nmr), list2.append(ida), list3.append(cid)

def idadema(self):

    for x in range (0, len(self)):

        if x == 0:
            mai_ida = self[x]
            mai_pos = x
        if self[x] > mai_ida:
            mai_ida = x
            mai_pos = x
 
    return mai_pos

def idademe(self):

    for x in range (0, len(self)):

        if x == 0:
            men_ida = self[x]
            men_pos = x
        if self[x] < men_ida:
            men_ida = x
            men_pos = x
    
    return men_pos

print(f'Cliente mais velho;\n\nNúmero: {list1[idadema(list2)]}\nIdade: {list2[idadema(list2)]}\nCidade: {list3[idadema(list2)]}\n')
print(f'Cliente mais novo;\n\nNúmero: {list1[idademe(list2)]}\nIdade: {list2[idademe(list2)]}\nCidade: {list3[idademe(list2)]}\n')