import mysql.connector

cadastro = mysql.connector.connect(
    host = '127.0.0.1',
    user = 'root',
    password = '',
    database = 'cadastro'
)

name =  input('insira seu nome: ')
namev = name.split()
c = cadastro.cursor()
c.execute ('create table if not exists teste( nome varchar (30) NOT NULL)')
add_user = ('insert into teste'
    '(nome)'
    'values(%s)')
data_user = (namev)
c.execute(add_user, data_user)
cadastro.commit()
c.close()
cadastro.close()