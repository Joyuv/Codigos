n1 = int(input('Insira a primeira nota: '))
n2 = int(input('Insira a segunda nota: '))

nf = (n1 + n2) / 2

if (nf >= 60):

    print('Parabéns você passou, sua média foi {}'.format(nf))

if (nf < 60):

    if (nf < 40):

        print('Que tristesa, você realmente estudou? Sua nota foi {}'.format(nf))

    if (nf >= 40 ):

        print('Que triste você ficou em recuperação, sua média foi {}'.format(nf))
