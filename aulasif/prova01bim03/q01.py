tam = int(input('insira o tamanho desejado para as listas: '))
lista1 = []
lista2 = []
iguais = []
iguaisp = ''
for x in range (0, tam):

    el = int(input('Insira um número para ser inserido na primeira lista: '))
    lista1.append(el)
    
for x in range (0, tam):
    
    el = int(input('Insira um número para ser inserido na segunda lista: '))
    lista2.append(el)

def comparacaoigu(lista1,lista2,iguais):
    for x in lista1:
        igual = 0
        for y in lista2:
            if x == y:
                igual += 1

    if igual >= 2:

        if x in iguais:
            pass
        else:
            iguais.append(x)

    return iguais



iguais = comparacaoigu(lista1, lista1, iguais)
iguais = comparacaoigu(lista2, lista2, iguais)

for x in lista1:

    if x in lista2:

        if x in iguais:
            pass
        else:          
            iguais.append(x)

for x in iguais:
    iguaisp += f'{x} '
print(f'Os valores que acabaram por se repetir nas listas são: ({iguaisp})')