"""
Tasks:
- Keep track of cards in hand
- Keep track of all cards played (suite/value/g or b)
- Keep track of number of cards each player has in order to keep track of score
- Create simple task to play
- Create a method to track the amount of cards other players have by counting how many cards they played/penalties
- Crate a function to determine the confidence score.
"""

prophet_points = 0
prophet_player = None

def reset_prophet():
    global prophet_points
    prophet_points, prophet_player = 0, None

def set_prophet(prophet):
    global prophet_player
    prophet_player = prophet

def turn_points():
    most_cards = max(other_player_cards)
    return [most_cards - other_player_cards[0], most_cards - other_player_cards[1], most_cards - other_player_cards[2], most_cards - other_player_cards[3]]

def post_turn(prophet_decision=3): 
    """ This function is called after each turn and it sets the updated # of points for each player. 
    prophet_decision = 1 if prophet made the RIGHT decision and player played the RIGHT card, 
    2 if prophet made the RIGHT decision and player played the WRONG card, 3 if prophet made the WRONG decision"""
    global other_player_points
    global prophet_points
    global prophet_player
   
    other_player_points = turn_points()
    if prophet_player is None:
        print("PROPHET PLAYER NONE")
        return

    other_player_points[prophet_player - 1] += prophet_points
    print(other_player_points)

    if(prophet_decision == 3):
        other_player_points[prophet_player - 1] -= prophet_points
        reset_prophet()
    else:
        prophet_points += prophet_decision
        other_player_points[prophet_player - 1] += prophet_decision

def calculate_points(most, your_cards):
    points = most - your_cards
    if (your_cards == 0):
        points += 4
    return points

def penalties(correct_play, cards): # ask server if correct play, delete parameters later if accessible from server directly
    if(correct_play):
        return -1 * cards
    else:
        return cards # ask server how mamy cards played


def calculate_cards(correct_play, cards, player): # delete parameters later if accessible from server directly
    # make new_cards negative to ensure it works
    # new_cards = represents cards discarded or penalty
    global other_player_cards
    other_player_cards[player-1] += penalties(correct_play, cards) # ask server how many cards played

#def determine_play:


cards_played = []
#cards_played.append([suite, value, good/bad (boolean)])
#suites = heart, club, diamonds, spades

cards_hand = []
other_player_points = [0,0,0,0]
other_player_cards = [14, 14, 14, 14]
#test data

print(other_player_cards)

calculate_cards(False, 4, 2)

other_player_points = turn_points()

set_prophet(3)

post_turn(1)
print(other_player_points)

"""
post_turn(1)
post_turn(3)

set_prophet(2)
post_turn(2)

print(other_player_points)
"""

#format of cards played


## This is an example of using imports

import PGSS
from PGSS import utils
from PGSS.utils import Mathy


print(Mathy.addTwo(5,5))
my_math = Mathy()
my_math.storeNumber(7)
print(my_math.addToSelf(10))