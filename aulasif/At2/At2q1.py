
altura  = float(input('insira sua altura atual, ou a ultima que lembra: '))
peso = float(input('insira o seu peso atual, por favor NÃO MINTA: '))

imc = peso / (altura ** 2)

if (imc > 18.5 and imc <= 25):

    print('parabéns seu peso está normal, você é massa.')

elif (imc > 25 and imc <= 29.9):

    print('você está com sobrepeso, por favor reveja sua indole.')

elif (imc >= 30 and imc <= 34.9):

    print('você está obeso, vai malhar não faça isso você devia repensar seus atos.')

elif (imc >= 35 and imc <= 39.9):

    print('meu mano, isso ae ta meio estranho, tem certeza que digitou o valor correto? bem se tiver tu ta com obesidade grau 2.')

elif (imc >= 40):

    print('que triste meu mano, tu vai morrer, tu ta com obesidade grau 3, por favor se dirija ao plano funerário e compre um caixão, bem grande.')

else :

    print('meu mano coma mais, você está um palito, e provavelmente anêmico, cuidado ae não coma mais')