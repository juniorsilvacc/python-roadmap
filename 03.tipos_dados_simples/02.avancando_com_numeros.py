# Conversões de tipos numericos 
numero_int = 10
numero_float = float(numero_int)
print(numero_float)

# Operações aritmetricas
a = 1
b = 3
c = 6
d = 2

print(a + b)
print(c - d)
print(a / b) # Divisão normal
print(b * c)
print(a // c) # Divisão inteira
print(a ** c)
print(c % d) # Modulo

# Precedentes
resultado = 3 + 4 * 5
print(resultado)

resultado2 = (3 + 4) * 5
print(resultado2)

op_complexas = (10 + 10) * 2 - (3 - 4)
print(op_complexas)

# Funções matematicas
numero = -15
numero_abs = abs(numero)
print(numero_abs)

numero_quebrado = 1.79234912
print(round(numero_quebrado))

base = 2
expoente = 5
modulo = 3
result = pow(base, expoente)
print(result)

# Modulo math
import math

numero = 16

raiz_qdr = math.sqrt(numero)
print(raiz_qdr)

print(math.pi)

# Números grandes
num_grande = 1.5e6 # 1500000
num_peq = 2.5e-3 # 0.0025

print(num_grande)
print(num_peq)