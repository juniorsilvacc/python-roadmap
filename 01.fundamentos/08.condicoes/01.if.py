# Se
idade = 18
if idade >= 18:
    print("É maior de idade")

# Se não
idade = 15
if idade >= 18:
    print("É maior de idade")
else:
    print("É menor de idade")

# if ... elif ... else
nota = 7
if nota >= 9:
    print("Excelente")
elif nota >= 7:
    print("Aprovado")
elif nota >= 5:
    print("Recuperação")
else:
    print("Reprovado")

# Operadores lógicos (and, or, not)
idade = 20
tem_carteira = True
if idade >= 18 and tem_carteira:
    print("Pode dirigir")
if not tem_carteira:
    print("Não pode dirigir")

# Verificar se número é par ou ímpar
numero = 4
if numero % 2 == 0:
    print("Par")
else:
    print("Ímpar")
