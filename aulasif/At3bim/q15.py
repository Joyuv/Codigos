lista1 = []
lista2 = []
lista3 = []

list1 = input('Insira números separados por espaço (ex.: 2 3 6): ')
list2 = input('Insira números separados por espaço (ex.: 2 3 6): ')

lista1 = list1.split()
lista2 = list2.split()

for x in lista1:

    for y in lista2:

        if x == y:
            
            for w in lista3:
            
                if x != w:
                    lista3.append(y)

                elif x == w:
                    ezequiel_corno = 1


print('Lista 3\n\n')

for z in lista3:

    print(z)
