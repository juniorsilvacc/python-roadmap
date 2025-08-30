import sqlite3

# 1 - Conectando com o DB
conexcao = sqlite3.connect('titulo.db')
cursor = conexcao.cursor()

# 2 - Leitura de Dados
dados = cursor.execute("SELECT * FROM filmes")

print(dados.fetchall())
cursor.close()