from datetime import datetime

# EXERCÍCIO 01
print("Olá, Mundo!")

# EXERCÍCIO 02
nome_usuario = str(input("Qual é seu nome? "))
print(f"Saudação, meu nome é {nome_usuario}!")

# EXERCÍCIO 03
if 18 >= 18:
    print("Você é de maior")
else:
    print("Você é de menor. Não pode dirigir")

# EXERCÍCIO 04
numero_01 = float(input("Digite um número: "))
numero_02 = float(input("Digite outro número: "))
soma = numero_01 + numero_02
print(f"A soma dos dois números é igual a {soma}")

# EXERCÍCIO 05
ano_atual = datetime.now().year
ano_nascimento = int(input("Qual ano você nasceu? "))
idade = ano_atual - ano_nascimento
print(f"Você tem {idade} anos de idade, com base no ano fornecido.")