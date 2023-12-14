a = int(input('insira o valor de linhas da matriz: '))
b = int(input('insira o valor de culunas da matriz: '))
m = []

#region Média e comparação
for x in range(a):
    linha = []
    for y in range(b):
        val = int(input(f'insira o valor da matriz ({x+1}, {y+1}): '))
        if y == 0:
            linha = [val]
        if y > 0:
            linha += [val]
    m.append(linha)
maiorp = 0
contp = 0
cont = 0
med = 0
for x in range(0, len(m)):
    for y in range(0, len(m[x])):
        if m[x][y] % 2 == 0:
            contp += 1
            if contp == 0:
                maiorp = m[x][y]
            if contp != 0:
                if m[x][y] > maiorp:
                    maiorp = m[x][y]
        cont += 1
        med += m[x][y]
med = med/cont
print(f'A média dos {cont} numeros na matriz é: {med}')
print(f'O maior número par da sua matriz é: {maiorp}')
#endregion
#region Transposição

novam = []

for x in range(b):
    linha = []
    for y in range(a):
        val = m[y][x]
        linha += [val]
    novam.append(linha)

print(f'A matriz transposta é: {novam}')
    
#endregion