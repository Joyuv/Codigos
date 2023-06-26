import mysql.connector

cadastro = mysql.connector.connect(
    host = '127.0.0.1',
    user = 'root',
    password = '',
    database = 'cadastro'
)

cursor = cadastro.cursor()

cursor.execute ('describe pessoas')

for x in cursor:
    print(x)