# Quando usar dict:
# Use quando você precisa mapear ou associar dados com nomes (chaves).
# É como uma tabela de informações em formato chave: valor

aluno = {
    "nome": "Carlos",
    "idade": 20,
    "notas": [8.5, 9.0, 7.2]
}

# Acessando os dados
print(aluno["nome"])       # Carlos
print(aluno["notas"][1])   # 9.0

print(aluno.get("idade"))  # 20

# Adicionando nova chave
aluno["curso"] = "Python"

# Alterando nome
aluno["nome"] = "Junior"

# Métodos úteis
# .keys() retorna todas as chaves
print(aluno.keys())

# values() → retorna todos os valores
print(aluno.values())

# .items() → retorna pares (chave, valor)
print(aluno.items())

# Percorrendo diciário
for chave, valor in aluno.items():
    print(f"{chave}: {valor}")

# Verificando se chave existe
print("nome" in aluno) # True


produtos = {
    "Arroz": 15.50,
    "Feijão": 8.90,
    "Macarrão": 6.75
}

print(sum(produtos.values()))

maior_valor = max(produtos, key=produtos.get)
print(maior_valor)

for produto, preco in produtos.items():
    print(f'{produto}: R$ {preco:.2f}')