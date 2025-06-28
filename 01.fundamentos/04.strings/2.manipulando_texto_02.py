linguagem = "Python"

print(linguagem[0])
print(linguagem[3])
print(linguagem[-1])

# endswith e startswith
print(linguagem.endswith("on"))
print(linguagem.startswith("Py"))
print(linguagem.startswith("Pyy"))

# Fatiamento de strings
texto = "O HTML dá-lhe a opção de adicionar cor, alterar a fonte, adicionar imagens e vídeos, e incluir hiperligações na sua mensagem."
novo_texto = texto[10:]
print(novo_texto)