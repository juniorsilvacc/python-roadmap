# Listas
lista_vazia = []

print(lista_vazia)
print(len(lista_vazia))

lista_01 = [1, 2, 3, 4, 5]
lista_02 = [6, 7, 8, 9, 10]

print(lista_01)
print(len(lista_01))

concatenar_listas = lista_01 + lista_02
print(concatenar_listas)


# Verificar se existe na lista (in e not in)
print(2 in lista_01)
print(6 not in lista_02)

# Modificar valores
lista_01[0] = 11
print(lista_01)

# Indice na lista
print(lista_01[1])