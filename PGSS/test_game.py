from game_player import Game
from game_player import Player

# Things to Include in our Test Game
# People playing cards correctly
# People playing cards incorrectly
# People becoming prophet
# Gaining points as prophet
# Not becoming prophet and losing points
# CHIPS?!?!?!

game = Game()
player = Player()

game.turn([(5,2)],True)
game.post_turn(game.players[0], True,1,3)

game.turn([(11,3),(2,1)],False)
game.post_turn(game.players[1], False,2,3)

print(game)



# game.players[0].post_turn(True,1,3)
# print(game.players[0].cards)

"""
print(player1.get_cards())


print("POINTS")
self.post_turn(player2, 1,4,2)

print("player1" + str(player1.get_points()))

self.set_prophet(player2)
print("prophet" + str(player2.get_points()))
self.post_turn(player1, 1,4,2)
print("player1" + str(player1.get_points()))

print("prophet" + str(player2.get_points()))

self.post_turn(player1, 1,4,2)

print("player1" + str(player1.get_points()))

print("prophet" + str(player2.get_points()))

self.post_turn(player1, 1,4,3)

print("player1" + str(player1.get_points()))

print("prophet" + str(player2.get_points()))
"""
