# ideia: criar um mercado com 7 produtos compraveis
# miojo, leite compensado, flokis mucirilo, sucrilhos de maracujá, maracujá, pinga, álcool 70.

pt = 0

a = 0

while (a == 0):

    p = input('Insira o nome do produto, miojo 3,00 , leite compensado 5,75 , flokis mucirilo 2,00 , sucrilhos de maracujá 4,50 , maracujá 0,75  pinga 5,00 , álcool 70. 7,00 , se \ndeseja fechar a compra digite fechar ')

    if (p == 'miojo'):

        print('o produto escolhido foi miojo')

        q = int(input('Quantos sacos você deseja levar? '))

        pt = q * 3.00

    if (p == 'leite compensado'):

        print('O produto escolhido foi o leite compensado')

        q = int(input('Quantas latas você deseja levar? '))

        pt = q * 5.75

    if (p == 'flokis mucirilo'):

        print('O produto escolhido foi flokis mucirilo')

        q = int(input('Quantos você deseja levar? '))

        pt = q * 2.00

    if (p == 'sucrilhos de maracujá'):

        print('O produto escolhido foi sucrilhos de maracujá')

        q = int(input('Quantos pacotes você deseja levar? '))

        pt = q * 4.50

    if (p == 'maracujá'):

        print('O produto escolhido foi maracujá')

        q = int(input('Quantos você deseja levar? '))

        pt = q * 0.75

    if (p == 'pinga'):

        print('O produto escolhido foi pinga')

        q = int(input('Quantos garrafas você deseja levar? '))

        pt = q * 5.00

    if (p == 'alcool 70'):

        print('O produto escolhido foi alcool 70')

        q = int(input('Quantos sacos você deseja levar? '))

        pt = q * 3.00

    if (p == 'fechar'):

        print('A sua compra deu {}R$'.format(pt))

    elif (p):

        print('seu produto não foi encontrado')

    

  


