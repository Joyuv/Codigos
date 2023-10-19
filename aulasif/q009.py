numero = int(input('insira um número a seguir maior que mil: '))
numerostr = str(numero)
nome = []
for x in numerostr:
    nome.append(x)
numerostr = ''
for i in range(len(nome)-1, -1, -1):
    numerostr += nome[i]
    print(numerostr)
numero = int(numerostr)
numero += 1000
print(numero)