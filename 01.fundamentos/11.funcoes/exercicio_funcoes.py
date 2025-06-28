def boletim(nome, nota):
    if nota >= 7:
        status = "Aprovado"
    elif nota >= 5:
        status = "Recuperação"
    else:
        status = "Reprovado"
    
    return f"{nome} está {status} com nota {nota}"

print(boletim("Ana", 8.5))
print(boletim("João", 4.7))
print(boletim("Carla", 5.8))