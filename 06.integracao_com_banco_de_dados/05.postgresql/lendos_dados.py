from conexao_postgres import conn

cursor = conn.cursor()

cursor.execute(
    """ 
        SELECT * FROM games;
    """
)

result = cursor.fetchall()
print(result)