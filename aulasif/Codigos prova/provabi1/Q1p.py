
a = int(input('insira um valor: '))
b = int(input('insira um segundo valor: '))
c = int(input('insira um terceiro e último valor: '))

if (a > b and a > c and b > c):

    print(f'seus valores em ordem decrescente é a seguinte ({a}) ({b}) ({c})')

if (a > b and a > c and c > b):

    print(f'seus valores em ordem decrescente ficou a seguinte ({a}) ({c}) ({b})')

if (b > a and b > c and a > c):

    print(f'seus valores em ordem decrescente ficou da seguinte maneira ({b}) ({a}) ({c})')

if (b > a and b > c and c > a):

    print(f'seus valores em ordem decrescente ficou organizada no seguinte padrão ({b}) ({c}) ({a})')

if (c > b and c > a and b > a):

    print (f'os valores inseridos foram reorganizados na ordem decrescente da seguinte maneira ({c}) ({b}) ({a})')

if (c > b and c > a and a > b):

    print (f'os valores inseridos foram reorganizados na ordem decrescente da seguinte maneira ({c}) ({a}) ({b})')