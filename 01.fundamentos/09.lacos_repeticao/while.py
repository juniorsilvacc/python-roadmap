# Usar o while quando a condição for verdadeira indefinidamente
# Usar qunado espera uma entrada e repetir até algo mudar
# Ela pode ser infinito se a condição não mudar

nomes = []
while True:
    nome = input("Digite seu nome: ")
    
    if nome == "Junior":
        break
    nomes.append(nome)

print("\nNomes digitados:")
for nome in nomes:
    print(nome)