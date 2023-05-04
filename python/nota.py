#obj: tirar média de um aluno com base em duas notas

#valor das notas
n1 = int(input('digite a primeira nota '))
n2 = int(input('digite a segunda nota '))

#calculo da média
m = (n1 + n2) / 2

#retorno do resultado
if (m >= 60):print('parabéns você foi aprovado com {} pontos'.format(m))
if (m < 60):print('se esforçe mais da próxima você reprovou com {} pontos'.format(m))
