texto = "Python é muito legal"
palavras = texto.split()
texto_invertido = " ".join(palavras[::-1])
print(texto_invertido)


texto1 = "arara"
texto2 = "ovo"

# Remover espaços e deixar em minúsculo
texto1_format = texto1.lower().replace(" ", "")
texto2_format = texto2.lower().replace(" ", "")

# Verificar se texto original é igual ao seu reverso
palindromo1 = texto1_format == texto1[::-1]
palindromo2 = texto2_format == texto2[::-1]

print(palindromo1)
print(palindromo2)