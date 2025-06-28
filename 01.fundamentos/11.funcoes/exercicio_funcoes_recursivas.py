def inverter(texto):
    if len(texto) == 0:
        return ""
    else:
        return texto[-1] + inverter(texto[:-1])

# Teste
print(inverter("python"))  # nohtyp
