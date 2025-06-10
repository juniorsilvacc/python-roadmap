#  Formatação
frase = "Python é muiTo boM"

print(frase.lower())
print(frase.upper())
print(frase.capitalize())

# Remoção de espaços
espacos = " Remocao de espaços  "

print(espacos.strip())

# Substituição de caracteres
subs_carecteres = "Hoje o dia será ótimo"
print(subs_carecteres.replace("o dia", "a noite"))

# Split para separar por ","
dados_separados = "nome,sobrenome,idade,email"
print(dados_separados.split(','))

# Acessando valor em lista
palavras_lista = ['Oi', 'Boa', 'Noite']
print(palavras_lista[1])