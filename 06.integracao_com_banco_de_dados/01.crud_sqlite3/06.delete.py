import sqlite3

# 1 - Conectando com o DB
conexcao = sqlite3.connect('titulo.db')
cursor = conexcao.cursor()

# 2 - Deletar Dados
id = 1
cursor.execute(
    """
        DELETE FROM filmes WHERE ID in (?)
    """,
    (id,)
)

conexcao.commit()
conexcao.close()

print('Dados excluidos com sucesso')