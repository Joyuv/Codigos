
n = int(input('insira a nota do aluno de 0 a 100: '))
f = int(input('insira o número de faltas deste aluno, de 0 a 100 também, não tente gracinhas: '))

if (n > 80 and n <= 100 and f <= 30 and f >= 0):

    print('parabéns você é um aluno dedicado, você passou de ano!')

if (n > 80 and n <=100 and f > 30 and f <= 100):

    print('que tristeza não é mesmo, tu é esperto mas faltou demais, agora vai rodar.')

if (n >= 60 and n < 80 and f <= 22 and f >= 0):

    print('que bom, você passou. mas por outro lado poderia ter feito melhor.')

if (n >= 60 and n < 80 and f > 22 and f <= 100):

    print ('você vai rodar, mais um ano olhando para as mesmas paredes.')

if (n >= 40 and n < 60 and f <= 30 and f >= 0):

    print('se salvou por pouco, boa sorte aí no próximo ano.')

if (n >= 40 and n < 60 and f > 30 and f <= 100):

    print('você infelizmente não fez por onde merecer passar, não veio a escola e não estudou.')

if (n < 40 and n >= 0):

    print('você não estudou o suficiente, boa sorte estudando mais no próximo ano, e tenta passar no próximo.')

if (n > 100 or n < 0 or f > 100 or f < 0):

    print('você tentou alguma gracinha né não?')