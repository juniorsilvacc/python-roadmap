nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
cnh = input("Possui carteira de motorista?(SIM/NÃO): ").lower()

# Verificar Idade
if idade < 0:
    print("Idade inválida")
else:
    if idade <= 12:
        classificacao = "Criança"
    elif idade <= 17:
        classificacao = "Adolescente"
    elif idade <= 59:
        classificacao = "Adulto"
    else:
        classificacao = "Idoso"
    
    # Pode dirigir?
    if idade >= 18 and cnh == "sim":
        habilitacao = "Pode dirigir"
    elif idade >= 18 and cnh == "não":
        habilitacao = "Não pode dirigir"
    else: 
        habilitacao = "Menor de idade, não pode dirigir"
    
    # Exibindo o resumo
    print("\n--- RESUMO DO CADASTRO ---")
    print(f"Nome: {nome}")
    print(f"Idade: {idade}")
    print(f"Classificação: {classificacao}")
    print(f"Situação de habilitação: {habilitacao}")