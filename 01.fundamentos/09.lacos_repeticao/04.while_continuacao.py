# Lista de filmes
filmes = ["Titanic", "The Godfather", "Inception", "Jurassic Park", "Interestrelar"]

# 1 - Interando valores de uma lista de filmes usando while
index = 0
while index < len(filmes):
    print(filmes[index])
    index += 1

# 2 - Quando a condição for atendida, o loop será encerrado
index = 0
while index < len(filmes):
    if filmes[index] == "Inception":
        break
    print(filmes[index])
    index += 1
    
# 3 - Quando a condição for atendida, o loop vai para  a próxima iteração
index = 0
while index < len(filmes):
    if filmes[index] == "Inception":
        index += 1
        continue
    print(filmes[index])
    index += 1

# 4 - Avaliação do filme com WHILE
movieName = input("Digiet o nome o do filme: \n")
movieRating = int(input("Digite quantas avaliações deseja fazer: \n"))

total = 0
count = 0

while count < movieRating:
    note = float(input("Digite a nota para o filme: \n"))
    total += note
    count += 1

if movieRating < 0:
    average = total / movieRating
else:
    average = 0
    
print(f"Média de avaliação do filme {movieName} é: {average:.2f}")