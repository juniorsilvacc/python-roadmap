# Criar dicionário vazio
produtos = {}

# Ler 3 produtos e preços
for i in range(3):
    nome = input("Digite o nome do produto: ")
    preco = float(input(f"Digite o preço de {nome}: "))
    produtos[nome] = preco   # chave = nome, valor = preço

# Imprimir o dicionário completo
print(produtos)

# Produto mais caro (pega a chave com maior valor)
produto_mais_caro = max(produtos, key=produtos.get)
print(produto_mais_caro)

# Média dos preços
media = sum(produtos.values()) / len(produtos)
print(f"{media:.2f}")
