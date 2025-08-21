# Classe Pai (Superclasse) - Generalista
class Game:
    total_games = 0 # Variável de classe para contar o número total de jogos

    # Construtor com atributos passado por parametro
    def __init__(self, name = "", yearLaunch = 0, multiplayer = 0, note = 0):
        self.name = name
        self.yearLaunch = yearLaunch
        self.multiplayer = multiplayer
        self.note = note
        Game.total_games += 1
        self.totalEvaluation = 0
        self.evaluators = 0
    
    def __str__(self):
        return f"Game: {self.name}"
    
    # Método
    def technical_sheet(self):
        print("### Dados do Jogo ###")
        print(f"Nome do jogo: {self.name}")
        print(f"Ano de Lançamento: {self.yearLaunch}")
        print(f"Nota: {self.note}")
    
    def evaluate(self, note):
        self.totalEvaluation += note
        self.evaluators += 1
    
    def average(self):
        print(f"Média do filme {self.name}: {self.totalEvaluation / self.evaluators}")

# Classe derivada (Subclasse) - Especializada
class SinglePlayerGame(Game):
    def __init__(self, name="", yearLaunch=0, note=0, storyLine=""):
        super().__init__(name, yearLaunch, multiplayer=False, note=note)
        self.storyLine = storyLine
    
    def technical_sheet(self):
        super().technical_sheet()
        print(f"Enredo: {self.storyLine}\n")

mult_game = Game("Fortnite", 2017, True, 9.5)
mult_game.technical_sheet()

sing_game = SinglePlayerGame("Elden Ring", 2022, 10.0, "Elden Ring é um jogo eletrônico de RPG de ação em terceira pessoa.")
sing_game.technical_sheet()