# Recursão é quando uma função chama a si mesma para resolver um problema menor

# Exemplo básico: contagem regressiva
def contagem_regressiva(n):
    if n <= 0:
        print("🚀 Decolar!")
    else:
        print(n)
        contagem_regressiva(n - 1)

contagem_regressiva(5)

# Fatorial (clássico da recursão)
def fatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fatorial(n - 1)

print(fatorial(5))

# Soma dos números até N
def soma_ate(n):
    if n == 1:
        return 1
    else:
        return n + soma_ate(n - 1)

print(soma_ate(4))  # 4 + 3 + 2 + 1 = 10

# Sequência de Fibonacci
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(6))  # 8
