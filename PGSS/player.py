
class Player():
    # def set_prophet(prophet):
    #     global prophet_player
    #     prophet_player = prophet
    # def reset_prophet():
    #     global prophet_points
    #     prophet_points, prophet_player = 0, None
    points = 0
    cards = 14

    def __init__(self, points=0, cards=14):
        self.points = points
        self.cards = cards

    def set_prophet(self,prophet):
        self.prophet = prophet
    
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
    