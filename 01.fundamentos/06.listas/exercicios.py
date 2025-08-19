# Criar uma lista vazia
numeros = []

# Ler 3 números inteiros do usuário e adicionar na lista
for i in range(3):
    n = int(input(f"Digite o {i+1}º número: "))
    numeros.append(n)

# Imprimir a lista completa
print(numeros)

# Imprimir o primeiro elemento da lista
print(numeros[0])

# Imprimir a soma de todos os elementos da lista
print(sum(numeros))
