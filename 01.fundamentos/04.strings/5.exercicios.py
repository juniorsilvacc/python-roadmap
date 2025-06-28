# Exercicio 01
frase = "Python é incrível"
frase_replace = frase

print(frase_replace.replace("incrível", "fantástico"))

# Exercicio 02
nome_completo = input("Digite seu nome completo: ")
partes = nome_completo.split()
primeiro_nome = partes[0]
ultimo_nome = partes[-1]

print(f"{primeiro_nome} {ultimo_nome}")

# Exercicio 03
lista_itens = input("Digite uma lista de itens separados por virgula: ")
lista_separada = lista_itens.split(",")
resultado = ";".join(lista_separada)

print(f"Itens formados: {resultado}" )

# Exercicio 04
from datetime import date

nome_usuario = input("Digite o seu nome: ")
data_atual = date.today().strftime("%d/%m/%Y")
mensagem = f"""
    Bem-vindo {nome_usuario}
    Hoje é {data_atual}
"""

print(mensagem)

# Exercicio 05
escrever_texto = input("Escreva um texto: ")
vogais = "aeiouAEIOU"
contador = sum(1 for char in escrever_texto if char in vogais)

print(f"Total de vogais: {contador}")