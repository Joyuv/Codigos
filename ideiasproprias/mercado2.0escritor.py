from itertools import count
from random import randint
class produto():
    id_obj = count()

    def __init__(self, nome, preco, terminacao):

        self.__id = next(produto.id_obj)
        self.__terminacao = terminacao
        self.__nomeproduto = nome
        self.__nome = f'==== {nome} '
        self.__preco = preco

    def get_id(self):
        return self.__id
    def get_terminacao(self):
        return self.__terminacao
    def get_nome(self):
        return self.__nome
    def get_nome_produto(self):
        return self.__nomeproduto
    def get_preco(self):
        return self.__preco
    
    def set_nome(self, nome):
        self.__nome = nome
    def set_preco(self, preco):
        self.__preco = preco

    def escolha_de_produto(self, sacola, tap, quant):

        print(f'\nVocê comprou: {quant} {self.get_terminacao()}(s) de {self.get_nome_produto()}\n')

        tap += self.get_preco() * quant
        sacola += f'{self.get_nome()}\t\t         {self.get_preco()} * {quant}\t====\n'

        return tap, sacola
        

#region produtos
maca = produto('Maçã', 0.79, 'unidade')
abacaxi = produto('Abacx.', 6.99, 'unidade')
feijao = produto('Feij.', 5.99, 'pacote')
leite = produto('Leit.', 3.99, 'caixa')
leite_em_po = produto('Leipo', 4.99, 'lata')
#endregion

tap = 0
sacola = ''

def receita(sacola, tap):
    num_receita = randint(0,1000000)
    with open(f'receita{num_receita}.txt', 'x') as f:
        f.write('====\t\t    Receita  \t\t\t====\n====\t\t    \t\t\t\t    ====\n')
        f.write('====\tMercadinho São Vincente \t====\n====\t\t        \t\t\t\t====\n')
        f.write('====\t\t      Produtos \t\t\t====\n====\t\t    \t\t\t\t    ====\n')
        f.write(f'{sacola}====\t\t        \t\t\t\t====\n')
        f.write('====\tMercadinho São Vincente \t====\n====\t\t        \t\t\t\t====\n')
        f.write(f'====\t Total a pagar: {tap:.2f}   \t====\n')
    sacola = ''

opcao = 0

while opcao != 2:

    produto_esc = 'nada'
    print('\n\t---Menu---\n\n1-Iniciar Sistema\n2-Sair Do Sistema\n')
    opcao = int(input('Insira a opção: '))
    print()

    if opcao == 1:
        
        print('\tOlá bem vindo!\n')

        while produto_esc.lower() != 'fechar':

            produto_esc = input('Insira o produto a seguir: ')
            produto_esc = produto_esc.lower()

            if produto_esc.lower() == 'fechar':
                break


            if produto_esc == 'maçã':
                quant = int(input('Insira a quantidade: '))
                tap, sacola = maca.escolha_de_produto(sacola, tap, quant)
            elif produto_esc == 'feijão':
                quant = int(input('Insira a quantidade: '))
                tap, sacola = feijao.escolha_de_produto(sacola, tap, quant)
            elif produto_esc == 'leite':
                quant = int(input('Insira a quantidade: '))
                tap, sacola = leite.escolha_de_produto(sacola, tap, quant)
            elif produto_esc == 'abacaxi':
                quant = int(input('Insira a quantidade: '))
                tap, sacola = abacaxi.escolha_de_produto(sacola, tap, quant)
            elif produto_esc == 'leite em pó':
                quant = int(input('Insira a quantidade: '))
                tap, sacola = leite_em_po.escolha_de_produto(sacola, tap, quant)
            else:

                print('Produto desconhecido, tente novamente.\n')

        receita(sacola, tap)

print('Tenha um bom dia!')