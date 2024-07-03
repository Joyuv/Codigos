palavral = []
invertida = []

while True:
    palavra = input('insira uma palavra a seguir: ')
    if palavra == 'parar' or palavra == 'Parar' or palavra == 'PARAR':
        break
    else:
        palavral.append(palavra)
    
    for x in palavra:
        invertida.append(x)

    invertida.reverse()
    palavrai = ''
    for x in invertida:
        palavrai = palavrai + x

    print(palavrai)
    invertida = []