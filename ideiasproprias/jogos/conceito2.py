print('Iniciar - 1\nSair - 2')

class player():

    def __init__(self, vida, chances):
        self.__vida = vida
        self.__chances = chances
    def set_vida(self, vida):
        self.__vida = vida
    def get_vida(self):
        return self.__vida
    def set_cha(self, chances):
        self.__chances = chances
    def get_chances(self):
        return self.__chances

opc = int(input('\nInsira sua escolha a seguir: '))

if opc == 2:
    print('Ok.')
if opc == 1:
    jogador1 = player(20, 3)