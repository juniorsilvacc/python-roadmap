cidades = ()

for i in range(3):
    cidade = input("Digite o nome da cidade: ")
    cidades = cidades + (cidade,) 

print(cidades)
print(cidades[-1])
print(len(cidades))
