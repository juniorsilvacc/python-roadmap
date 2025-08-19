# 1 - Função que imprime um nome completo
def full_name(first_name, last_name):
    print(f'{first_name} {last_name}')

full_name("Cicero", "Júnior")

# 2 - Função para somar dois números
def sum_numbers(a, b):
    return a + b

soma = sum_numbers(10, 20)
print(f'A soma de A + B: {soma}')

# 3 - Função com parâmetro default
def address(country = "Brasil"):
    return country

print(address())
print(address("Argentina"))

# 4 - Função para avaliar filme
def rate_movie(num_ratings, movie_name):
    total = 0
    for i in range(num_ratings):
        note = float(input("Digite a nota para o filme: "))
        total += note
    
    if num_ratings > 0:
        average = total / num_ratings
    else:
        average = 0

    print(f"A média de avaliações do filme {movie_name} é {average:.2f}")

rate_movie(2, "MadMax")