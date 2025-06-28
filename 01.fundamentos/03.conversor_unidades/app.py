import conversor

def conversor_temperaturas():
    conversor.menu()
    opcao = input("Digite a opção desejada (1/2/3): ")
    
    if opcao == "1":
        celsius = float(input("Digite a temperatura em Celsius: "))
        fahreinheit = conversor.celsius_para_fahrenheit(celsius)
        print(f"{celsius:.2f}C é equivalente a {fahreinheit:.2f}F")
    elif opcao == "2":
        fahreinheit = float(input("Digite a temperatura em Fahreinheit: "))
        celsius = conversor.fahreinheit_para_celsius(fahreinheit)
        print(f"{fahreinheit:.2f}F é equivalente a {celsius:.2f}C")
    elif opcao == "3":
        print("Obrigado por utilizar o conversor!")
    else:
        print("Opçãoo inválida. Digite 1, 2 ou 3.")

# Serve para indicar o ponto de entrada principal do seu programa.
if __name__ == '__main__':
    conversor_temperaturas()

# Esse bloco é usado para executar o código apenas quando o arquivo for executado diretamente.
# Ou seja, tudo que estiver dentro do if será executado nesse caso.

# Este arquivo é o principal, responsável por chamar as funções importadas de outros arquivos.
