
v = float(input('insira o preço do produto: '))
m = 'placeholdergenérico'
while (m != 'fatura' and m != 'avista'):
    m = input('vai ser no vencimento da fatura ou à vista? (fatura) (avista) ')

    if (m == 'fatura' and v <= 1000 ):

        vd = v - (v * (15 / 100))

        print(f'o preço com o desconto ficou de {vd}')

    if (m == 'fatura' and v > 3000 ):

        vd = v - (v * (30 / 100))

        print(f'o preço com o desconto ficou de {vd}')

    if (m == 'avista' and v <= 1000 ):

        vd = v - (v * (23 / 100))

        print(f'o preço com o desconto ficou de {vd}')

    if (m == 'avista' and v > 1000 and v <= 2000 ):

        vd = v - (v * (25 / 100))

        print(f'o preço com o desconto ficou de {vd}')

    if (m == 'avista' and v > 3000 ):
        
        vd = v - (v * (30 / 100))

        print(f'o preço com o desconto ficou de {vd}')

    if (m == 'avista' or m == 'fatura' and v > 2000 and v <= 3000): 

        print(f'o preço deu {v}')

    if (m != 'avista' and m != 'fatura'):

        print('tu escreveu errado ae volta no código e escreve certo.')