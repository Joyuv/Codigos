#peso e gênero

h = float(input('insira a sua altura.'))

g = (input('insira o seu gênero. (Homen) / (Mulher)'))

if (g == 'homen' and g == 'Homen'):

    print ('seu peso ideal é {:.2f}'.format((72.7 * h) - 58))

if (g == 'mulher' and g == 'Mulher'):

    print ('seu peso ideal é {:.2f}'.format((62.1 * h) - 44.7))