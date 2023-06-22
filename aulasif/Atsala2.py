y = 0

c = int(input('insira o valor mínimo (não conta com ele): '))

f = int(input('insira o valor máximo (não conta com ele): '))

for x in range (c, f):


    if (x % 2) == 0:

        y = y + x
    

print(y)