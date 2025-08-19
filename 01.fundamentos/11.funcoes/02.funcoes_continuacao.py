# 1 - Função para calcular a média de notas
def calculate_avarage():
    num_ratings = int(input("Digite quantas avaliações deseja fazer pro filmes: "))
    total = 0
    for i in range(num_ratings):
        note = float(input("Digite a nota para o filme: "))
        total += note
    
    if num_ratings > 0:
        average = total / num_ratings
    else:
        average = 0
    
    return average

print(f"A média de avaliações é: {calculate_avarage():.2f}")

# 2 - Função para cadastrar um filme:
def create_movie():
    name = input("Digite o nome do filme: ")
    yearLaunch = int(input("Digite o ano de lançamento do filme: "))
    moviePrice = float(input("Digite o preço do filme: "))
    rating = float(input("Digite a nota do filme: "))
    print(f"{name} ({yearLaunch}) - R$ {moviePrice:.2f}")

create_movie()