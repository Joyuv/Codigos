#obj: ler a quantidade de dinheiro que uma pessoa tem na carteira e mostrar quantos dolares ela pode comprar cotação 5,06

d = float(input('quanto dinheiro você tem na carteira? '))

do = d // 5.06

print('com seu dinheiro você pode comprar {} e lhe sobrará {:.2f}'.format(do, d % 5.06))