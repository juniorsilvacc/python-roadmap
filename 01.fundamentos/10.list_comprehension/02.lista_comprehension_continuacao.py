# Lista de filmes
filmes = ["Titanic", "The Godfather", "Inception", "Jurassic Park", "Interestrelar"]

listComprehension = [i for i in range(10) if i < 4]
print(listComprehension)

listFilmes = [movie.upper() for movie in filmes]
print(listFilmes)

# Filmes que possuem a letra "e" no título
movieWithE = [movie for movie in filmes if "e" in movie.lower()]
print(movieWithE)

# Filmes que eu assisti
movie_watched = [movie for movie in filmes if movie != "Interestrelar"]
print(movie_watched)

# Encontrando um filme pelo nome
moviesList = ["Titanic", "The Godfather", "Inception", "Jurassic Park", "Interestrelar"]
while True:
    searchName = input("Digite o nome do filme para buscar na lista (ou Sair para encerrar): \n")
    if searchName.lower() == "sair":
        print("Programa encerrado")
        break
    
    # O if está dizendo: “se o nome que o usuário digitou (searchName) aparecer dentro do título do filme (movie)
    # então adiciona esse filme na nova lista (foundMovies).”
    foundMovies = [movie for movie in moviesList if searchName.lower() in movie.lower()]
    if foundMovies:
        print(f"Filme encontrado com o nome: {searchName}")
    else:
        print("Não foi encontrado")