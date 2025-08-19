numeros = set()

for i in range(5):
    numero = int(input(f"Digite {i+1}º número "))
    numeros.add(numero)

print(numeros)
print(len(numeros))
print(max(numeros))