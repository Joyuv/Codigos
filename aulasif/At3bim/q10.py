#Propriedade de Giva

print('=====================================================================================\nBem vindo ao show do milhão (pobre), todas as perguntas elaboradas pelos meus amigos.\n=====================================================================================')

escolha = input('\nInsira qualquer coisa que não seja (sair) para começar. ')

if escolha != 'sair':

    class jogador ():

        def __init__(self, pontosq):
            self.__pontosq = pontosq

        def get_pontos(self):
            return self.__pontosq
        def set_pontos(self, pontosq):
            self.__pontosq = pontosq

    jogador1 = jogador(0.0)

    class questao ():

        def __init__(self, pergunta, resposta, valor):
            self.__pergunta = pergunta
            self.__resposta = resposta
            self.__valor = valor
            self.__fazer_pergunta = (f'A pergunta de R${self.get_valor()}: {self.get_pergunta()}')

        def get_pergunta(self):
            return self.__pergunta
        def get_resposta(self):
            return self.__resposta
        def get_valor(self):
            return self.__valor

        def fazer_pergunta(self):
            return self.__fazer_pergunta

        def show_de_show(self):

            while True:

                print (self.fazer_pergunta())

                resposta = input('Resposta: ')

                if resposta == self.get_resposta():
                    print('\nParabéns! Você acertou!\n')
                    jogador1.set_pontos(jogador1.get_pontos() + self.get_valor())

                    break
                if resposta != self.get_resposta():
                    print(f'Você errou, tente novamente, você sofreu uma penalidade de {self.get_valor()/2}')
                    jogador1.set_pontos(jogador1.get_pontos() - self.get_valor()/2)

#================================================================================================================================================================================
#Mexa nisso aqui para mudar ou adicionar na exata ordem (pergunta -> resposta -> pontos) ex.: pergunta4('mudarpergunta', 'mudarresposta', mudarpontos (fora de aspas pois é int))
    pergunta1 = questao('\nQual o melhor time do brasil? (digite em minúsculo)', 'palmeiras', 4)
    pergunta2 = questao('\nO palmeiras tem mundial? (digite em minúsculo)', 'sim', 8)
    pergunta3 = questao('\nQual o melhor país para se viver no mundo? (digite em minúsculo)', 'brasil', 16)
#Mexa nisso aqui para mudar ou adicionar na exata ordem (pergunta -> resposta -> pontos) ex.: pergunta4('mudarpergunta', 'mudarresposta', mudarpontos (fora de aspas pois é int))
#================================================================================================================================================================================
#Propriedade de Giva
#=======================================================================================================================================================
#Sempre que adicionar uma pergunta nova adiciona aqui também (nome_da_variavel_pergunta_no_bloco_acima.show_de_show(OS PARENTESES SÂO IMPORTANTISSIMO))
    pergunta1.show_de_show()
    pergunta2.show_de_show()
    pergunta3.show_de_show()
#Sempre que adicionar uma pergunta nova adiciona aqui também (nome_da_variavel_pergunta_no_bloco_acima.show_de_show(OS PARENTESES SÂO IMPORTANTISSIMO))
#=======================================================================================================================================================

    print(f'Acabou, você acaba de ganhar R${jogador1.get_pontos()} em barras de ouro que valem mais do que dinheiro.')

else:

    print('Até um outro dia.')