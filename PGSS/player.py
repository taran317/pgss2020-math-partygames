import game

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

    def update_prophet():
        prophet = game.prophet



    def get_cards():
        return(self.cards)
    def get_points():
        return(self.points)
    def turn_points():
        most_cards = max(other_player_cards)
        return (most_cards - self.cards)

    def calculate_points(self, most):
        self.points = most - self.cards
        if (self.cards == 0):
            self.points += 4
        return self.points

    def calculate_cards(correct_play, new_cards): # delete parameters later if accessible from server directly
        # make new_cards negative to ensure it works
        # new_cards = represents cards discarded or penalty
        cards += penalties(correct_play, new_cards) # ask server how many cards played