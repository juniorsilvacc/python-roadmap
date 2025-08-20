# Classe
class Game:    
    # Construtor com atributos passado por parametro
    def __init__(self, name = "", yearLaunch = 0, multiplayer = 0, note = 0):
        self.name = name
        self.yearLaunch = yearLaunch
        self.multiplayer = multiplayer
        self.note = note
        self.totalEvaluation = 0
        self.evaluators = 0
    
    def __str__(self):
        return f"Game: {self.name}"
    
    # Método
    def technical_sheet(self):
        print("### Dados do Jogo ###")
        print(f"Nome do jogo: {self.name}")
        print(f"Ano de Lançamento: {self.yearLaunch}")
        print(f"Nota: {self.note}\n")
    
    def evaluate(self, note):
        self.totalEvaluation += note
        self.evaluators += 1
    
    def average(self):
        print(f"Média do filme {self.name}: {self.totalEvaluation / self.evaluators}")

# Objeto sendo instanciado
game1 = Game("Elden Ring", 2021, False, 10.0)
game2 = Game("Fortnite", 2017, True, 95.0)

# Método sendo chamado
game1.technical_sheet()
game2.technical_sheet()

game1.evaluate(9.0)
game1.evaluate(10.0)