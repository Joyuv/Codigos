arq = open('/home/giva/Codigos/aulasif/R. K./imp.txt', 'r')
arq2 = open('/home/giva/Codigos/aulasif/R. K./par.txt', 'r')

# for x in range (1, 1001):
#     arq.write(str(x) + '\n')

numeros = arq.readlines() + arq2.readlines()

listanova = []

for item in numeros:
    listanova.append(int(item.replace('\n', '')))

numeros = sorted(listanova)

arq = open('/home/giva/Codigos/aulasif/R. K./numeros.txt', 'w')

for item in numeros:
    arq.write(str(item) + '\n')

arq.close()