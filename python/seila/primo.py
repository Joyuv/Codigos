intervalo = int(input('insira o intervalo (0, x): '))

for x in range (1, intervalo+1):
    primo = 0
    if x == 1:
        print(x)
    if x != 1:
        for y in range (1, x+1):
            if x % y == 0:
                primo += 1
        if primo > 2:
            pass
        else:
            print(x)
    
        
        