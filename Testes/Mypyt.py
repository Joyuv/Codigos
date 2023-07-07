import mysql.connector
from mysql.connector import Error
def conectar():
    try:
        conexão = mysql.connector.connect(
            host = '127.0.0.1',
            user = 'root',
            password = '',
            database = 'cad'
        )
        if conexão.is_connected():
            print('Conexão Bem-Sucedida! ')
            return conexão
    except Error as e:
        print(f'Erro ao carregar a base de dados: {e}')

opc = input('(cadastro) ou (login)? ')

conexão = conectar()
if opc == 'cadastro':
    usuario = input('insira o nome de usuario: ')
    senha = input('insira sua senha: ')

    def cadastrar (usuario, senha):
        try:

            c = conexão.cursor()
            query = 'INSERT INTO usuario (usuario, senha) VALUES (%s, %s)'
            dados_usuario = (usuario, senha)
            c.execute (query, dados_usuario)
            conexão.commit()
            print('Cadastro Bem-sucedido! ')
        
        except Error as e:
            print(f'Erro ao cadastrar o usuário: {e}')

    cadastrar  (usuario, senha)

if opc == 'login':

    usuario = input('insira o nome de usuario: ')
    senha = input('insira sua senha: ')

    def login (usuario, senha):
        try:
            c = conexão.cursor()
            query = 'SELECT * FROM usuario WHERE usuario = %s AND senha = %s'
            dados_login = (usuario, senha)
            c.execute (query, dados_login)
            usuario = c.fetchone()

            if usuario:
                print('Deu Certo! ')
            else:
                print('Não Deu Certo :( ')
        except Error as e:
            print('Deu um Erro repita ai')

    login (usuario, senha)