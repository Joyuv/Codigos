lista1, lista2, soma = [], [], 0

for x in range (0,5):

    lista1.append(int(input('Insira o número da primeira lista: ')))
    lista2.append(int(input('Insira o número da segunda lista: ')))

for x in range (0,5):

    soma = (lista1[x] * lista2[x]) + soma

print(lista1), print(soma), print(lista2)