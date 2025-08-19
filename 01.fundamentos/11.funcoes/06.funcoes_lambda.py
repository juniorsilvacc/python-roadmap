# É uma função anônima (sem nome) usada para tarefas simples e rápidas, geralmente em uma linha.

# Função normal
def soma(x):
    return x + 2
print(soma(2))

# Função Lambda
soma = lambda x: x + 2
print(soma(2))

# Lambda dentro de map() — dobrar valores
numeros = [1, 2, 3, 4]
dobrados = list(map(lambda x: x * 2, numeros))
print(dobrados)  # [2, 4, 6, 8]

# Lambda com filter() — filtrar pares
numeros = [1, 2, 3, 4, 5, 6, 8]
pares = list(filter(lambda x: x % 2 == 0, numeros))
print(pares)  # [2, 4, 6]

# Lambda com sorted() — ordenar por tamanho do nome
nomes = ["Maria", "João", "Ana", "Gabriela"]
ordenados = sorted(nomes, key=lambda nome: len(nome))
print(ordenados)  # ['Ana', 'João', 'Maria', 'Gabriela']

# Lambda com if...else (condicional)
nota = 8
status = (lambda x: "Aprovado" if x >= 7 else "Reprovado")(nota)
print(status)  # Aprovado
