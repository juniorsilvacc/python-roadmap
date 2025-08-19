# Adicionando elementos
# Append -> adiciona no final da lista
animais = ["Gato", "Cachorro", "Pássaro"]
animais.append("Cavalo")
print(animais)

# Insert -> especifica a posição onde será adicionado
animais.insert(1, "Peixe")
print(animais)

numeros = []
numeros.append(5) # Adiciona no final da lista
numeros.insert(1, 10) # Especifica a posição onde irá ser adicionado
print(numeros)

# Removendo elementos
# Remove -> Remove o elemento especifico (Indice que não existe gera erro)
animais.remove("Gato")
print(animais)

# Pop -> Remove o último elemento
animais.pop()
print(animais)

filmes = ['As branquelas', 'Se bebre não case I', 'Se bebre não case II', 'Se bebre não case III']
filmesCopy = filmes.copy()
filmesCopy.remove('As branquelas')
print(filmesCopy)

