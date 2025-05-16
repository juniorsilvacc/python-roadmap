# Exercício 01
num1 = int(input("Digite um número: "))
num2 = int(input("Digite outro número: "))

print(f"Soma {num1 + num2}")
print(f"Subtração {num1 - num2}")
print(f"Multiplicação {num1 * num2}")
print(f"Divisão {num1 / num2}")

# Exercício 02
num_flutuante = float(input("Digite um número flutuante: "))
print(f"{round(num_flutuante)}")

# Exercício 03
num_inteiro = 3
num_inteiro = float(num_inteiro)
num_float = int(num_inteiro)
print(num_inteiro)
print(num_float)

# Exercício 04
import math

print("Digite três números")
a = float(input("Digite o primeiro número (a): "))
b = float(input("Digite o segundo número (b): "))
c = float(input("Digite o terceiro número (c): "))

delta = (b ** 2) - 4 * a * c
print(f"Delta: {delta}")

if delta < 0:
    print("Não existe raiz quadrada")
elif delta == 0:
    x = -b / (2 * a)
    print(f"Raiz única {x}")
else: 
    raiz_delta = math.sqrt(delta)
    x1 = (-b + raiz_delta) / (2 * a)
    x2 = (-b - raiz_delta) / (2 * a)
    print(f"Raízes reais: x1 = {x1}, x2 = {x2}")

# Exercício 05
print("Área do círculo")
raio = float(input("Digite o raio: "))
area = math.pi * raio ** 2
print(f"A área do círculo é {area:.2f}")