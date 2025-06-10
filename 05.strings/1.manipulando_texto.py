# String
linguagem = "Python"
versao = "3.12"
frase = "O python é ótimo"

print(linguagem, versao, frase)

# Concatenação
concatenacao = linguagem + " " + versao + " " + frase
print(concatenacao)

repeticao = "Olá " * 3
print(repeticao)

# Atribuição 
linguagem_secundaria = "Javascript"
linguagem = linguagem_secundaria
print(linguagem)

# Quantidade de caractere
print(len(linguagem))

# Verificar se existe string em texto
frase_texto = "O HTML dá-lhe a opção de adicionar cor, alterar a fonte, adicionar imagens e vídeos, e incluir hiperligações na sua mensagem."
print("HTML" in frase_texto)
print("Frase" in frase_texto)