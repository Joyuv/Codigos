s = int(input('qual é o seu salário? '))

a = s * (15 / 100)
ns = s + a

if(ns >= 1320):print('parabéns você recebeu um aumento de 15 porcento seu salário agora é de {}'.format(ns))
if(ns < 1320):print('procure seus direitos você está recebendo muito pouco, seu novo salário com o aumento de 15 porcento é de {}'.format(ns))