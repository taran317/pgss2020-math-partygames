from PGSS.player import player

class Game():
    def start_game():
        player1 = 
    def calculate_points(most, your_cards):
        points = most - your_cards
        if (your_cards == 0):
            points += 4
        return points

    def calculate_cards(correct_play, cards, player): # delete parameters later if accessible from server directly
        # make new_cards negative to ensure it works
        # new_cards = represents cards discarded or penalty
        global other_player_cards
        other_player_cards[player-1] += penalties(correct_play, cards) # ask server how many cards played

    def penalties(correct_play, cards): # ask server if correct play, delete parameters later if accessible from server directly
        if(correct_play):
            return -1 * cards
        else:
            return cards # ask server how mamy cards played  

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