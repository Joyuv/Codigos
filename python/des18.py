import math

an = float(input('digite um valor em graus: '))

sen = math.sin(math.radians(an))
cos = math.cos(math.radians(an))
tan = math.tan(math.radians(an))

print('O seno cosseno e tangente de {} graus são respectivamente: {:.2f} / {:.2f} / {:.2f}'.format(an, sen, cos, tan))
