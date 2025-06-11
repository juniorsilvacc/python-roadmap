# Recebedor um texto
# E determinar quanta: palavras, caracteres e linhas o texo tem
def analisar_texto(texto):
    # Contar linhas
    linhas = texto.splitlines()
    numero_linhas = len(linhas)
    
    # Contar palavras
    palavras = texto.split()
    numero_palavras = len(palavras)
    
    # Contar caracteres
    numero_caracteres = len(texto)
    
    return numero_linhas, numero_palavras, numero_caracteres # Retornando uma tupla com 3 valores
    # Ou fazer usando dict
    # return {
        #"linhas": numero_linhas   
    #}

def main():
    print("Bem-vindo ao analisador de textos!")
    print("Digite o seu texto abaixo, e para fnalizar pressone Enter duas vezes")
    
    texto = ""
    while True:
        linha = input()
        # Condição de encerramento
        if linha == "":
            break
        texto += linha + "\n"
        
    linhas, palavras, caracteres = analisar_texto(texto) # Desacoplando a tupla
    
    print("Resultado análise: ")
    print(f"Número de linhas {linhas}")
    print(f"Número de palavras {palavras}")
    print(f"Número de caracteres {caracteres}")

if __name__ == "__main__":
    main()
    
# O laço while roda até que o usuário digite uma linha vazia (Enter sem digitar nada).
# Cada linha digitada é adicionada (concatenada) à variável 'texto'.
# A expressão texto += linha é igual a texto = texto + linha.
# Isso serve para juntar todas as linhas em uma única string.