import mysql.connector

conexao = mysql.connector.connect(
    host='#########',
    user='#######',
    password='############',
    database='####',
)

cursor = conexao.cursor()

# CRUD:

# CREAT
# nome_produto = "Apple MacBook Pro M4 Pro"
# valor = 1720000
# comando_creat = f'INSERT INTO vendas (nome_produto, valor) VALUES ("{nome_produto}", {valor})'
# cursor.execute(comando_creat)
# conexao.commit() # quando está a editar o banco de dados

# READ
# comando_read = f'SELECT * FROM vendas'
# cursor.execute(comando_read)
# resultado = cursor.fetchall() # quando está a ler o banco de dados
# print(resultado)

# UPDATE
# valor = 8700
# nome_produto = "Durag"
# comando_update = f'UPDATE vendas SET valor = {valor} WHERE nome_produto = "{nome_produto}"'
# cursor.execute(comando_update)
#conexao.commit() # quando está a editar o banco de dados

# DELETE
nome_produto = "Apple MacBook Pro M4 Pro"
comando_delete = f'DELETE FROM vendas WHERE nome_produto = "{nome_produto}"'
cursor.execute(comando_delete)
conexao.commit()

cursor.close()
conexao.close()