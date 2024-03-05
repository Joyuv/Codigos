import info
from datetime import date
import pickle


arquivo_open_r = open('/home/giva/Codigos/ideiasproprias/Gerenciador-de-atividades/info.py', 'r')

class atividade:

    def __init__(self, numero, nome, descricao, data_entrega):
        self.__numero = numero
        self.__nome = nome
        self.__descricao = descricao
        self.__data_entrega = data_entrega

#region get_set
    def get_nome(self):
        return self.__nome
    def get_descricao(self):
        return self.__descricao
    def get_data_entrega(self):
        return self.__data_entrega
    def get_numero(self):
        return self.__numero
    
    def get_numero(self, numero):
        self.__numero = numero
    def set_nome(self, nome):
        self.__nome = nome
    def set_descricao(self, descricao):
        self.__descricao = descricao
    def set_data_entrega(self, data_entrega):
        self.__data_entrega = data_entrega
#endregion

def adicionar():
    nome = input('Insira o nome da atividade: ')
    descricao = input('Insira o descrição: ')
    data_e = input('Insira o data de entrega: ')


    # quant = info.quant
    quant = 1
    # data = [quant]
    # path = 'data.pickle'
    # with open(path, 'wb') as file:
    #     pickle.dump(data, file)
    # arquivo_open_w = open('/home/giva/Codigos/ideiasproprias/Gerenciador-de-atividades/info.py', 'a')
    # arquivo_open_w.write()
    # arquivo_open_w.close()

def menu():
    print('''               Menu                

1-Adicionar atividade
2-Remover Atividade
3-Ver atividades''')

    escolha = input('\nEscolha uma opcção para continuar (ex: 1): ')

    if escolha == '1':
        adicionar()

menu()

arquivo_open_r.close()