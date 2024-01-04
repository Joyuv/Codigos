gaba = ['a', 'c', 'b', 'e', 'e', 'b', 'a', 'a', 'c', 'b']
respostas = []
matriculas = []
def comparacao(matriz, lista_comp, aluno):
    points = 0
    for x in range(len(matriz[aluno])):
        if matriz[aluno][x] == lista_comp[x]:
            points += 1
    return points
        

alun = int(input('Insira a quantidade de alunos: '))

for x in range(len(gaba)):
    print(f'Resposta do gabarito para a questão {x+1}: {gaba[x]}')

for x in range(alun):
    lin = []
    mat = [input(f'Insira a matricula do aluno {x+1}: ')]
    for y in range (len(gaba)):
        resp = [input(f'Insira a resposta do aluno {x+1} para a questão {y+1}: ')]
        lin += resp
    respostas.append(lin)
    matriculas.append(mat)

for x in range (len(respostas)):
    print(f'Resultado do aluno {x+1}\nMatricula: {matriculas[x][0]}\nRespostas: {respostas}\nPontuação: {comparacao(respostas, gaba, x)}\n')