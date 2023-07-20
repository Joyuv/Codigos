lista = []
soma = 0
ct = 0

while True:
    nome = input('Insira um nome ae: ')
    if nome != 'parar':
        altura = float(input('insira tua altura ae: '))
        soma = altura + soma
        ct +=1
        alturas = str(altura)
        nome = nome + ' '
        nomea = nome + alturas

        lista.append (nomea)
    if nome == 'parar':
        break
    
med = soma/ct
for nomes in lista:
    print (nomes)
print (f'A média das alturas é {med}')