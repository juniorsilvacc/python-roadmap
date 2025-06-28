# Um set é como uma "lista especial"
# Ele guarda múltiplos valores (como uma lista), mas sem repetições, e sem garantir ordem.
valores = set()
valores.add("João")
valores.add("Maria")
valores.add("João")  # não será adicionado novamente
print(valores)  # {'João', 'Maria'}

# Criando um set
frutas = {"maçã", "banana", "laranja", "maçã"}
print(frutas)  # {'banana', 'laranja', 'maçã'} (sem repetição)

frutas.add("uva") # Adicionando item
frutas.remove("banana") # Removendo item

# Operações de conjuntos
a = {1, 2, 3}
b = {3, 4, 5}
print(a | b)  # união: {1, 2, 3, 4, 5}
print(a & b)  # interseção: {3}

nomes = ["joão", "ana", "joão", "maria", "ana"]
nomes_unicos = set(nomes)  # Remover duplicatas
print(nomes_unicos)

# OBS:
a = {"uva", "banana"}         # ← Isso é um `set`
b = {"nome": "Carlos"}        # ← Isso é um `dict`

vazio = {}         # Isso é um **dicionário vazio**
vazio_set = set()  # Forma correta de criar um **set vazio**


