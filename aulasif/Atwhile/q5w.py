for x in range (0,5):
    numc = 0
    num = int(input('insira um número a seguir: '))
    while numc < num :
        numc += 1
        print(numc, )
    if x == 4:
        print('Cabou os laços')
    if x < 4:
        print('Mais laços')
        