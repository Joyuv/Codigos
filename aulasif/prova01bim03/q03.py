consoantes = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']
vogais = ['a','e','i','o','u']
vogaisp = []
novapalavra = ''
consoantesp = []
palavra = input('insira sua palavra a seguir: ')
palavra = palavra.lower()
for x in palavra:

    if x in consoantes:
        if x in consoantesp:
            pass
        else:
            consoantesp.append(x)
    if x in vogais:
        if x in vogaisp:
            pass
        else:
            vogaisp.append(x)
print(f'A palavra possui {len(vogaisp)} vogais e {len(consoantesp)} consoantes :)')

for x in palavra:


    if x in vogais:
        letra = vogais[vogais.index(x)]
        letra = letra.upper()
        novapalavra += letra
    elif x in consoantes:
        novapalavra += x

print(f'A nova palavra ficou assim: {novapalavra}')

print(f'As listas criadas foram:\nConsoantes: {consoantesp}\nVogais: {vogaisp}')