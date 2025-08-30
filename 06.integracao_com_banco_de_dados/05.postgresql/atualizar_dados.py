from conexao_postgres import conn

cursor = conn.cursor()

sql = """
    UPDATE games SET name = %s WHERE id = %s
"""

cursor.execute(sql, ("Fifa", 1,))
conn.commit()
print("Dados atualizados com sucesso")
conn.close()