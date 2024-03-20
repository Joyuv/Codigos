imp = open('/home/giva/Codigos/aulasif/R. K./imp.txt', 'a')
par = open('/home/giva/Codigos/aulasif/R. K./par.txt', 'a')

for x in range(1,1001):
    if x % 2 == 0:
        par.write(str(x)+ '\n')
    else:
        imp.write(str(x)+ '\n')

