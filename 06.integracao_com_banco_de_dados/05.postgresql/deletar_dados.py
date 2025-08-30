from conexao_postgres import conn

cursor = conn.cursor()

sql = """
    DELETE FROM games WHERE id = %s
"""

cursor.execute(sql, (2,))
conn.commit()
print("Dados excluidos com sucesso")
conn.close()