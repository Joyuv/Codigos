a = int(input("insira um valor"))
b = int(input("insira um valor"))
c = int(input("insira um valor"))

if (b > a):

    aux = b
    b = a
    a = aux

if (c > b):

    aux = c
    c = b
    b = aux

if (b > a):

    aux = b
    b = a
    a = aux

print(f"Sua ordem reorganizada ficou a seguinte ({a}) ({b}) ({c})")
