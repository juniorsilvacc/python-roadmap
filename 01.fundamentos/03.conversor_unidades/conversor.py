# Converter celsius para F
# Converter F para C

def celsius_para_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahreinheit_para_celsius(fahreinheit):
    return (fahreinheit - 32) * 5/9

def menu():
    print("Bem-vindo ao Conversor")
    print("Escolha uma opção:")
    print("1 - Converter de Celsius para Fahreinheit")
    print("2 - Converter de Fahreinheit para Celsius")
    print("3 - Sair")