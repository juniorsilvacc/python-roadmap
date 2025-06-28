filmes = [
    {"nome": "Matrix", "nota": 9.2},
    {"nome": "Interestelar", "nota": 8.7},
    {"nome": "Clube da Luta", "nota": 9.0},
    {"nome": "Coringa", "nota": 8.5},
    {"nome": "Avatar", "nota": 7.8}
]

soma = 0
melhor = filmes[0]
pior = filmes[0]

for filme in filmes:
    print(f"{filme['nome']} — Nota: {filme['nota']}")
    soma += filme["nota"] # Saída -> soma = 0 + filme[9.2] -> soma = 9.2 + filme[8.7]...
    
    if filme["nota"] > melhor["nota"]:
        melhor = filme
    if filme["nota"] < pior["nota"]:
        pior = filme

media = soma / len(filmes)

print(f"\nMédia das notas: {media:.1f}")
print(f"Melhor filme: {melhor['nome']} ({melhor['nota']})")
print(f"Pior filme: {pior['nome']} ({pior['nota']})")