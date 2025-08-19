# Lista de filmes
filmes = ["Titanic", "The Godfather", "Inception", "Jurassic Park", "Interestrelar"]

# 1 - Iterando valores a uma lista
for filme in filmes:
    print(filme)

# 2 - Quando a condição for atendida, o loop será encerrado (BREAK)
for filme in filmes:
    if filme == "Inception":
        break
    print(filme)
    
# 3 - Quando a condição for atendida, o loop vai para próxima iteração (CONTINUE)
for filme in filmes:
    if filme == "The Godfather":
        continue
    print(filme)
    
# Avaliação de filme
movieName = input("Digiet o nome o do filme: \n")
movieRating = int(input("Digite quantas avaliações deseja fazer: \n"))

total = 0
for i in range(movieRating):
    note = float(input("Digite a nota para o filme: \n"))
    total = total + note

if movieRating > 0:
    average = total / movieRating
else:
    average = 0

print(f"Média de avaliação do filme {movieName} é: {average:.2f}")