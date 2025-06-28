# Laço de repetição FOR
filmes = [
    "Matrix",
    "Interestelar",
    "Clube da Luta",
    "O Senhor dos Anéis",
    "Coringa",
    "Homem-Aranha",
    "Vingadores: Ultimato"
]

for filme in filmes:
    print(filme)

# Exibir os filmes com numeração
for i, filmes in enumerate(filmes, start=1):
    print(f"{i}. {filmes}")

# Exibir só os filmes com mais de 12 caracteres
for filme in filmes:
    if len(filme) > 12:
        print(f"Filme longo: {filme}")

# Mostrar os nomes em maiúsculo
for filme in filmes:
    print(filme.upper())

# Verificar se "Matrix" está na lista
for filme in filmes:
    if filme == "Coringa":
        print("Filme coringa está na lista")
        break

# Criar nova lista com apenas os filmes que contêm a letra "a"
filmes_com_letra_a = []
for filme in filmes:
    if "b" in filme.lower():
        filmes_com_letra_a.append(filme)
print(f"Filmes com a letra 'a': {filmes_com_letra_a}")