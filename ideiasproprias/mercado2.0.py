from itertools import count

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
        sacola += f'{self.get_nome()}\t\t     {self.get_preco()} * {quant}\t====\n'

        return tap, sacola
        

#region produtos
maca = produto('Maçã', 0.79, 'unidade')
feijao = produto('Feijão', 5.99, 'pacote')
leite = produto('Leite', 3.99, 'caixa')
#endregion

tap = 0
sacola = ''

def receita(sacola, tap):

    print('====\t\t  Receita  \t\t====\n====\t\t    \t\t\t====') #\n====\t\t    \t\t\t====
    print('====\t  Mercadinho São Vincente \t====\n====\t\t    \t\t\t====')
    print('====\t\t  Produtos \t\t====\n====\t\t    \t\t\t====')
    print(f'{sacola}====\t\t    \t\t\t====')
    print('====\t  Mercadinho São Vincente \t====\n====\t\t    \t\t\t====')
    print(f'====\t    Total a pagar: {tap:.2f} \t====')

produto_esc = 'nada'
opcao = 0

while opcao != 2:

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

            else:

                print('Produto desconhecido, tente novamente.\n')

        receita(sacola, tap)

print('Tenha um bom dia!')