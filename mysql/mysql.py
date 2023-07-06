import mysql.connector

cad = mysql.connector.connect(
    host = '127.0.0.1',
    user = 'root',
    password = '',
    database = 'cad'
)

usuario = input('insira o nome de usuario: ')
senha = input('insira sua senha: ')
usuariov = usuario.split()
senhav = senha.split()
c = cad.cursor()
add_user = ('insert into usuario'
    '(usuario, senha)'
    'values(%s, %s)'
)
insert_user = (usuariov, senhav)
c.execute(add_user, insert_user)
cad.commit()