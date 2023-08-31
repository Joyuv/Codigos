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

def cadastrar (usuario, email, senha):
    try:

        c = conexão.cursor()
        query = 'INSERT INTO usuario (usuario, email, senha) VALUES (%s,%s, %s)'
        dados_usuario = (usuario, email, senha)
        c.execute (query, dados_usuario)
        conexão.commit()
        print('Cadastro Bem-sucedido! ')
        
    except Error as e:
        print(f'Erro ao cadastrar o usuário: {e}')


def login (email, senha):
    try:
        c = conexão.cursor()
        query = 'SELECT * FROM usuario WHERE email = %s AND senha = %s'
        dados_login = (email, senha)
        c.execute (query, dados_login)
        usuario = c.fetchone()
        if usuario:
            print('Deu Certo! ')
            buscaid = 'SELECT * FROM usuario WHERE id = %s'
            id_usuario = (buscaid)
            
        else:
            print('Não Deu Certo :( ')
    except Error as e:
        print('Deu um Erro repita ai')


def cadastrar_receita_personalizada (usuario_id, qui, forma_resolução):
    try:
        c = conexão.cursor()
        query =  'INSERT INTO receitas (usuario_id, receita, forma_resolução) VALUES (%s, %s, %s)'
        inserir_dados = usuario_id, qui, forma_resolução
        c.execute (query, inserir_dados)
        conexão.commit()
        print('Formula inserida com sucesso!') 
    except Error as e:
        print('Deu erro ao cadastrar, tente novamenta outro dia')

def pegador_de_receita(id_usuario, qui):
    try:
        c = conexão.cursor()
        query = 'SELECT forma_resolução FROM receitas WHERE id_usuario = %s AND receita = %s'
        dados_busca = (id_usuario, qui)
        c.execute (query, dados_busca)
        forma_resolução = c.fetchall()
    
        return forma_resolução

    except Error as e:
        print(f'Deu errado a inserção dos dados: {e}')
        return None
def exibir_quimico (id_usuario):

    qui = 'nada'
    while qui != 'sair':
        qui = input('\nInsira o químico desejado: ')

        #elementos
        ir = '\niron'
        car = '\ncarbon'
        rad = '\nradium'
        pot = '\npotassium'
        sil = '\nsilicon'
        hyd = '\nhydrogen'
        oxy = '\noxygen'
        sug = '\nsugar'
        pho = '\nphosphorus'
        pla = '\nplasma'
        #químicos
        dex = [oxy, pla]
        dylo = [pot, sil, hyd]
        hyro = ['\n(dylovene)', rad]
        ina = [sug, oxy, car]
        bica = ['\n(inaprovaline)', car]
        kelo = [car, sil]
        derma = ['\n(kelotane)', oxy, pho]
        dexp = ['\n(dex)', ir, car]
        trico = ['\n(inaprovaline)', '\n(dylovene)']
        #casos
        if qui == 'dex' and 'dexalin' in qui:
            for quis in dex:
                print(quis)
                forma_resolução = input('Insira seu modo de resolver esta mistura: ')
                receitas = pegador_de_receita (id_usuario, qui)
                cadastrar_receita_personalizada (id_usuario, qui, forma_resolução )
                print('Formas de resolução')
                for forma in receitas:
                    print(forma[0])
        elif qui == 'hyro' and 'hyronalin' in qui:
            for quis in dylo:
                print(quis)
            for quis in hyro:
                print(quis)
                forma_resolução = input('Insira seu modo de resolver esta mistura: ')
                receitas = pegador_de_receita (id_usuario, qui)
                cadastrar_receita_personalizada (id_usuario, qui, forma_resolução )
                print('Formas de resolução')
                for forma in receitas:
                    print(forma[0])
        elif qui == 'dylo' and 'dylovene' in qui:
            for quis in dylo:
                print(quis)
                forma_resolução = input('Insira seu modo de resolver esta mistura: ')
                receitas = pegador_de_receita (id_usuario, qui)
                cadastrar_receita_personalizada (id_usuario, qui, forma_resolução )
                print('Formas de resolução')
                for forma in receitas:
                    print(forma[0])
        elif qui == 'ina' and 'inaprovaline' in qui:
            for quis in ina:
                print(quis)
            forma_resolução = input('Insira seu modo de resolver esta mistura: ')
            receitas = pegador_de_receita (id_usuario, qui)
            cadastrar_receita_personalizada (id_usuario, qui, forma_resolução )
            print('Formas de resolução')
            for forma in receitas:
                print(forma[0])
        elif qui == 'bica' and 'bicaridina' in qui:
            for quis in ina:
                print(quis)
            for quis in bica:
                print(quis)
            forma_resolução = input('Insira seu modo de resolver esta mistura: ')
            receitas = pegador_de_receita (id_usuario, qui)
            cadastrar_receita_personalizada (id_usuario, qui, forma_resolução )
            print('Formas de resolução')
            for forma in receitas:
                print(forma[0])
        elif qui == 'kelo' in qui:
            for quis in kelo:
                print(quis)
                forma_resolução = input('Insira seu modo de resolver esta mistura: ')
                receitas = pegador_de_receita (id_usuario, qui)
                cadastrar_receita_personalizada (id_usuario, qui, forma_resolução )
                print('Formas de resolução')
                for forma in receitas:
                    print(forma[0])
        elif qui == 'derma' in qui:
            for quis in kelo:
                print(quis)
            for quis in derma:
                print(quis)
                forma_resolução = input('Insira seu modo de resolver esta mistura: ')
                receitas = pegador_de_receita (id_usuario, qui)
                cadastrar_receita_personalizada (id_usuario, qui, forma_resolução )
                print('Formas de resolução')
                for forma in receitas:
                    print(forma[0])
        elif qui == 'bica' in qui:
            for quis in ina:
                print(quis)
            for quis in bica:
                print(quis)
                forma_resolução = input('Insira seu modo de resolver esta mistura: ')
                receitas = pegador_de_receita (id_usuario, qui)
                cadastrar_receita_personalizada (id_usuario, qui, forma_resolução )
                print('Formas de resolução')
                for forma in receitas:
                    print(forma[0])
        elif qui == 'dex+' in qui:
            for quis in dex:
                print(quis)
            for quis in dexp:
                print(quis)
                forma_resolução = input('Insira seu modo de resolver esta mistura: ')
                receitas = pegador_de_receita (id_usuario, qui)
                cadastrar_receita_personalizada (id_usuario, qui, forma_resolução )
                print('Formas de resolução')
                for forma in receitas:
                    print(forma[0])
        elif qui == 'trico' in qui:
            for quis in ina:
                print(quis)
            for quis in dylo:
                print(quis)
            for quis in trico:
                print(quis)
                forma_resolução = input('Insira seu modo de resolver esta mistura: ')
                receitas = pegador_de_receita (id_usuario, qui)
                cadastrar_receita_personalizada (id_usuario, qui, forma_resolução )
                print('Formas de resolução')
                for forma in receitas:
                    print(forma[0])

        elif qui == 'sair':
            print('\naté um outro dia')

        else:
            print('\nquímico desconhecido (tente abreviar)')
        
def menu_principal ():
    opc = input('(cadastro) ou (login)? ')
    conexão = conectar()

    if opc == 'cadastro':
        usuario = input('insira o nome de usuario: ')
        email = input('insira o email: ')
        senha = input('insira a senha desejada: ')

        cadastrar (usuario, email, senha)

    if opc == 'login':
        email = input('insira seu email: ')
        senha = input('insira sua senha: ')

        id_usuario = login(email, senha)
        
        exibir_quimico(id_usuario)

menu_principal ()