#ideia: banco super simples com saldo saque e depósito
nome = input('Qual é o seu nome caro cliente? ')

sal = 0

sair = 0

print('Olá {}! seja bem vindo(a) ao nosso banco\n\nque tipo de operação deseja fazer? digite saldo para ver seu saldo, saque para fazer um saque, depósito para efetuar um depósito e sair para sair daconta\n'.format(nome))

while(sair < 1):

    print('\n')

    ope = input('digite a operação em letras minusculas e sem acentos ')

    print('\n')

    if ope == 'saque':
        
        sa = float(input('digite o valor do saque '))

        sal = sal - sa

    elif ope == 'deposito':

        de = float(input('digite o valor do depósito '))

        sal = sal + de

    elif ope == 'saldo':

        print('o seu saldo é de {:.2f}'.format(sal))

    elif ope == 'sair':

        print('você escolheu sair, tenha um ótimo dia!')

        sair = 1

    else :

        print('operação invalida por favor tente novamente')
