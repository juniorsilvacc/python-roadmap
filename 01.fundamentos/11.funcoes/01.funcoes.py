# Uma função é um bloco de código reutilizável que executa uma tarefa. Em Python, usamos def para definir uma função.

# Função básica (sem argumento)
def saudacao():
    print("Olá! Bem-vindo ao sistema.")

saudacao()

# Função com 1 argumento
def saudacao(nome):
    print(f"Olá, {nome}!")

saudacao("Júnior")

# Função com múltiplos argumentos
def soma(a, b):
    return a + b

resultado = soma(5, 3)
print("Resultado da soma:", resultado)

# Função com valor padrão (default)
def saudacao(nome="Visitante"):
    print(f"Olá, {nome}!")

saudacao()          # Olá, Visitante!
saudacao("Bruno")   # Olá, Bruno!

#Função com *args (vários argumentos posicionais)
def somar_tudo(*numeros):
    return sum(numeros)

print(somar_tudo(1, 2, 3, 4))  # 10

# Avançado: função dentro de função
def operacao_matematica(op, a, b):
    def soma(x, y):
        return x + y
    def subtrai(x, y):
        return x - y

    if op == "soma":
        return soma(a, b)
    elif op == "subtrai":
        return subtrai(a, b)

print(operacao_matematica("soma", 10, 5))     # 15
print(operacao_matematica("subtrai", 10, 5))  # 5



