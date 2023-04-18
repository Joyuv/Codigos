#ditar uma série de números e quando ele fala 0 o número anterior é cancelado.

a = 0

b = 0

x = 0

r = 0

while(x < 5):
    
    c = b

    b = a

    a = int(input('insira um número'))


    if (a == 0):

        r = r - b

        p = int(input('Desejas apagar denovo?'))

        if(p == 0):

            r = r - c
    
        x = x + 1

              

        

    if (a > 0):
        
        r = r + a

        x = x + 1

        
print('o valor final é {}'.format(r))

