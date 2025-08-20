# Classe
class Game:
    name = ""
    yearLaunch = 0
    multiplayer = False
    note = 0
    
# Objeto
# Primeiro Jogo
game1 = Game()
game1.name = "Elden Ring"
game1.yearLaunch = 2021
game1.multiplayer = False
game1.note = 10.0

# Segundo Jogo
game2 = Game()
game2.name = "PUBG: BATTLEGROUNDS"
game2.yearLaunch = 2017
game2.multiplayer = True
game2.note = 9.70

print("### Dados do Jogo ###")
print(f"Nome do jogo: {game1.name} \nAno de Lançamento: {game1.yearLaunch} \nNota: {game1.note}")
print("######")
print(f"Nome do jogo: {game2.name} \nAno de Lançamento: {game2.yearLaunch} \nNota: {game2.note}")