numero = int(input('insira um número a seguir maior que mil: '))
numerostr = str(numero)
reversenumstr = ''
nome = []
for x in numerostr:
    nome.append(x)
for i in range(len(nome)-1, -1, -1):
    reversenumstr += nome[i]

if reversenumstr == numerostr:
    print('É palíndromo!')
if reversenumstr != numerostr:
    print('Não é palíndromo!')
