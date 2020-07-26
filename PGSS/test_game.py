from game_player import Game
from game_player import Player
from bot import Bot

# Things to Include in our Test Game
# People playing cards correctly
# People playing cards incorrectly
# People becoming prophet
# Gaining points as prophet
# Not becoming prophet and losing points
# CHIPS?!?!?!

game = Game()
player = Player()
bot = Bot()

print(bot.update_cards(game))
# game.get_good_cards()

game.turn(game.players[0],[(5,2)],True)
print(game)
game.turn(game.players[1],[bot.bot_turn(game)],False)
print(game)
game.turn(game.players[2],[bot.bot_turn(game)],False)
print(game)
game.turn(game.players[3],[bot.bot_turn(game)],True)
print(game)
game.turn(game.players[0],[bot.bot_turn(game)],False)
print(game)
game.turn(game.players[1],[bot.bot_turn(game)],True)
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
