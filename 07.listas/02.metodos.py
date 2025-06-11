# Adicionando elementos

# Append -> No final da lista
animais = ["Gato", "Cachorro", "Pássaro"]
animais.append("Cavalo")
print(animais)

# Insert -> Entre os elementos (especificar posição)
animais.insert(1, "Peixe")
print(animais)

numeros = []
numeros.append(5)
numeros.insert(0, 10)

print(numeros)

# Removendo elementos

# Remove -> Remove o elemento especifico (Indice que não existe gera erro)
animais.remove("Gato")
print(animais)

# Pop -> Remove o último elemento
animais.pop()
print(animais)