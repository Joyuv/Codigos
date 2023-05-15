
segundosv = int(input('Insira um valor em segundos.'))

h = segundosv // 3600

s = segundosv % 3600

m = s // 60

s = s - (m  * 60)

print (h, 'h', m, 'm', s, 's')