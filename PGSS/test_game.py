import eleusis_client
from eleusis_client import ApiClient
from game_player import Game
from game_player import Player
# from bot import Bot

# Things to Include in our Test Game
# People playing cards correctly
# People playing cards incorrectly
# People becoming prophet
# Gaining points as prophet
# Not becoming prophet and losing points
# CHIPS?!?!?!

def make_game():
    client = ApiClient("https://cheatcardgame.com")
    client.login('Tarzan','PGSS')
    pregame = client.create_game(False)
    print(client.add_oracle_bot(pregame.game_id))
    print(client.add_player_bot(pregame.game_id))
    print(client.add_player_bot(pregame.game_id))
    client.start_game(pregame.game_id)
    hand = client.get_hand(pregame.game_id)
    print(hand)
    print(client.get_game_state(pregame.game_id))

make_game()
# client.add_oracle_bot(pregame.game_id)
# pregame = client.add_player_bot(pregame.game_id)
# result = client.start_game(game_id)
# print(result)
# print(client.get_game_state(game_id))
# print(pregame)


game = Game()
player = Player()
# bot0 = Bot()
# bot1 = Bot()
# bot2 = Bot()
# bot3 = Bot()

# game.bot.update_good_cards([(1,2)])
# print(game.bot.get_good_cards())
# print("\n\n\n\n\n\n====================================================================\n\n\n\n\n\n")
# print("NEW ROUND\n")
# game.turn(game.players[0],[game.bot.bot_turn()],False)
# print(game)
# game.turn(game.players[1],[game.bot.bot_turn()],True)
# print(game)
# game.turn(game.players[1],[game.bot.bot_turn()],True)
# print(game)

# game.turn(game.players[1],[bot1.bot_turn(game)],False)
# print(game)
# game.turn(game.players[2],[bot2.bot_turn(game)],True)
# print(game)
# game.turn(game.players[3],[bot3.bot_turn(game)],False)
# print(game)
# print('ROUND TWO\n')
# game.turn(game.players[0],[bot0.bot_turn(game)],False)
# print(game)
# game.turn(game.players[1],[bot1.bot_turn(game)],False)
# print(game)
# game.turn(game.players[2],[bot2.bot_turn(game)],True)
# print(game)

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
