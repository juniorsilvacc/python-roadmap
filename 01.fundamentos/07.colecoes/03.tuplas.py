tupla1 = (10, 20, 30)
print(tupla1)

# Acessando elementos
tupla = ("maçã", "banana", "laranja")
print(tupla[0])  # maçã
print(tupla[2])  # laranja

# Tupla com tipos diferentes
pessoa = ("João", 30, 1.75, True)
print(pessoa)

# Desempacotando tuplas
nome, idade, altura = ("Maria", 25, 1.65)
print(nome)   # Maria
print(idade)  # 25
print(altura) # 1.65

# Usando funções e retornando multiplos
def operacao (a, b):
    return a + b, a - b

soma, subtracao = operacao(10, 5)
print("Soma:", soma)
print("Subtração:", subtracao)