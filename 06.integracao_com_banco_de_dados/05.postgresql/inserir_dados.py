from conexao_postgres import conn

cursor = conn.cursor()

games = [
    ('Interestrelar', 2014, 10.0),
    ('Sherek 2', 2001, 9.0)
]

for game in games:
    cursor.execute(
        """
            INSERT INTO games(name, year, score)
            VALUES (%s, %s, %s)
        """, game
    )
conn.commit()
print('Dados inseridos com sucesso!')
conn.close()