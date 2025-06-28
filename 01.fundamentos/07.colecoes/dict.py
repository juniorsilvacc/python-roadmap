# Quando usar dict:
# Use quando você precisa mapear ou associar dados com nomes (chaves).
# É como uma tabela de informações em formato chave: valor

aluno = {
    "nome": "Carlos",
    "idade": 20,
    "notas": [8.5, 9.0, 7.2]
}

print(aluno["nome"])       # Carlos
print(aluno.get("idade"))  # 20
print(aluno["notas"][1])   # 9.0

# Adicionando nova chave
aluno["curso"] = "Python"

# Iterando
for chave, valor in aluno.items():
    print(f"{chave}: {valor}")
