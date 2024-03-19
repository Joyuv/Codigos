consoantes = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
vogais = ['a', 'e', 'i', 'o', 'u']

while True:
    letra = input('insira uma letra do alfabeto, digite "fim" para parar: ')

    if letra.lower() == 'fim':
        break
    if letra.lower() in vogais:
        print('é vogal.')
    elif letra.lower() in consoantes:
        print('é consoantes.')
    else:
        print('letra desconhecida.')
    print('')