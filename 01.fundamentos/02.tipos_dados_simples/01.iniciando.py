# Números inteiros
numero1 = 42
numero2 = 50

print (f"Número {numero1}, {numero2}")

print(type(numero1))

valor_absoluto = abs(numero1)
print(valor_absoluto)

expo = pow(numero1, 2)
print(expo)

soma = numero1 + numero2
print(f"Soma: {soma}")

# Artimetrica
a = 160
b = 15

soma = a + b
multiplicacao = a * b
divisao_inteira = a // b # Divisão inteira
divisao_normal = a / b # Divisão normal
subtracao = a - b
resto = a % b

print("S: ", soma)
print("M: ", multiplicacao)
print("D - inteira: ", divisao_inteira)
print("D - normal: ", divisao_normal)
print("Sub: ", subtracao)
print("Resto: ", resto)

contador = 1
contador += 10
print(contador)

# Float
temperatura = 39.8
print("Temperatura: ", temperatura)
print(type(temperatura))

y = 3.3
x = 4.1
print(y + x)

# Arredondar 
numero = 2.61231
num_arredondar = round(numero, 2)
print(num_arredondar)

# Biblioteca math
import math

valor = 8.6

valor_acima = math.ceil(valor)
valor_abaixo = math.floor(valor)

print(f'Valor acima {valor_acima} - Valor abaixo {valor_abaixo}')

# Ponto flutuante
ponto_decimal = 0.2 + 0.3
print(f"Ponto decimal: {ponto_decimal:.2f}")
