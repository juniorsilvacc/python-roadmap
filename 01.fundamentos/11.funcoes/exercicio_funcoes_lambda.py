alunos = [
    {"nome": "Ana", "nota": 8.5},
    {"nome": "Bruno", "nota": 6.2},
    {"nome": "Carla", "nota": 9.1},
    {"nome": "Daniel", "nota": 5.8},
    {"nome": "Eduarda", "nota": 7.0}
]

aprovados = list(filter(lambda aluno: aluno['nota'] >= 7, alunos))
for aluno in aprovados:
    print(f"{aluno["nome"]} - {aluno["nota"]} - APROVADO")