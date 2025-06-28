# List comprehension é uma forma rápida e concisa de criar listas a partir de loops e condições.

# Estrutura básica
# nova_lista = [expressão for item in coleção]

# Jeito comum
numeros = [1, 2, 3, 4, 5]
dobrados = []

for n in numeros:
    dobrados.append(n * 2)
print(dobrados)

# Jeito com list comprehension
numeros = [1, 2, 3, 4, 5]
dobrados = [n * 2 for n in numeros]
print(dobrados)

# Transformar nomes em maiúsculo
frutas = ["Maça", "Banana", "Abacaxi", "Uva", "Abacate"]
maiusculos = [fruta.upper() for fruta in frutas]
print(maiusculos)

# Criar lista de filmes com nota maior que 8
filmes = [
    {"nome": "Matrix", "nota": 9.2},
    {"nome": "Avatar", "nota": 7.5},
    {"nome": "Coringa", "nota": 8.6}
]

# Criar lista de filmes com nota maior que 8
bons_filmes = [filme['nome'] for filme in filmes if filme['nota'] > 8]
print(bons_filmes)

alunos = [
    {"nome": "Ana", "nota": 8.5},
    {"nome": "Bruno", "nota": 6.2},
    {"nome": "Carla", "nota": 9.1},
    {"nome": "Daniel", "nota": 7.0},
    {"nome": "Eduarda", "nota": 5.8},
    {"nome": "Felipe", "nota": 4.3},
    {"nome": "Giovana", "nota": 10.0}
]

listando = [f"{aluno['nome']} — {aluno['nota']}" for aluno in alunos]
print(listando)

# Nota acima de 7
nota_acima_7 = [aluno['nota'] for aluno in alunos if aluno['nota'] > 7]
print(nota_acima_7)

# Aluno aprovado
aprovado = ["Aprovado" if aluno['nota'] >= 7 else "Reprovado" for aluno in alunos]
print(aprovado)

# Quando o if fica no começo → Condição ternária (if...else)
# ["Aprovado" if nota >= 7 else "Reprovado" for nota in notas]

# Quando o if fica no final → Filtro 
# [nota for nota in notas if nota >= 7]

# Quando não tem if, você está apenas transformando 
# # [nome.upper() for nome in nomes]