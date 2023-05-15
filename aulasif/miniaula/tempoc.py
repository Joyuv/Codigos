
h0 = int(input('insira o tempo que ele saiu (hora): '))

m0 = int(input('Insira o tempo que ele saiu (minuto): '))

s0 = int(input('insira o tempo que ele saiu (segundos): '))

h1 = int(input('Insira o tempo em que ele chegou (hora): '))

m1 = int(input('insira o tempo em que ele chegou (minuto): '))

s1 = int(input('insira o tempo em que ele chegou (segundos): '))

hf = h1 - h0

mf = m1 - m0

sf = s1 - s0

print('Você passou', hf, 'h', mf, 'm', sf, 's')
