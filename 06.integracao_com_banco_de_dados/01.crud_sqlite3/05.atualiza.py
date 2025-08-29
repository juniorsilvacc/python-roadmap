import sqlite3

# 1 - Conectando com o DB
conexcao = sqlite3.connect('titulo.db')
cursor = conexcao.cursor()

# 2 - Atualizar Dados
id = 1
cursor.execute(
    """
        UPDATE filmes 
        SET nome = ?, nota = ? 
        WHERE id = ?
    """,
    ("Homem Aranha", 9.8, id)
)

conexcao.commit()
conexcao.close()

print('Dados atualizados')