# Classe
class Game:    
    def __init__(self, name = "", yearLaunch = 0, multiplayer = 0, note = 0):
        self.name = name
        self.yearLaunch = yearLaunch
        self.multiplayer = multiplayer
        self.note = note
    
    def __str__(self):
        return f"Game: {self.name}"

game1 = Game("Elden Ring", 2021, False, 10.0)
game2 = Game("Fortnite", 2017, True, 95.0)

print("### Dados do Jogo ###")
print(f"\nNome do jogo: {game1.name} \nAno de Lançamento: {game1.yearLaunch} \nNota: {game1.note}")
print(f"\nNome do jogo: {game2.name} \nAno de Lançamento: {game2.yearLaunch} \nNota: {game2.note}")