import sqlite3

# 1- Conectando ao banco de dados
def conecta_db():
    conexao = sqlite3.connect('titulo.db')
    cursor = conexao.cursor()

    # Criando a tabela
    cursor.execute(
        """
            CREATE TABLE filmes (
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                ano INTEGER NOT NULL,
                nota REAL NOT NULL
            );
        """
    )
    return conexao

# 2 - Inserindo dados
def inserir_dados(nome, ano, nota):
    conexao = conecta_db()
    cursor = conexao.cursor()
    cursor.execute(
        """
            INSERT INTO filmes(nome, ano, nota) VALUES (?, ?, ?)
        """, (nome, ano, nota)
    )
    conexao.commit()
    conexao.close()

# 3 - Listagem de dados
def obter_dados():
    conexao = conecta_db()
    cursor = conexao.cursor()
    cursor.execute(
        """
            SELECT * FROM filmes
        """
    )
    dados = cursor.fetchall()
    conexao.close()

    return dados