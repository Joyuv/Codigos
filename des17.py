import math

co = float(input('digite o valor do cateto oposto: '))
ca = float(input('digite o valor do cateto adjecente: '))

hi = math.sqrt((co ** 2) + (ca ** 2))

print('a hipotenusa é igual a {}'.format(hi))