
class Game():
    prophet = None
    prophet_decision =   3
    current_board = { }

    def __init__(self):
        player1 = Player()
        player2 = Player()
        player3 = Player()
        player4 = Player() 
        player1.get_cards()
        player1.get_cards()
        player1.get_points()

    def update_current_board(new_cards): #Gets the new cards from the server and upates them to the board
        self.current_board += new_cards
    
    def set_prophet(self,prophet):
        self.prophet = prophet

   
    
    def penalties(correct_play, cards): # ask server if correct play, delete parameters later if accessible from server directly
        if(correct_play):
            return -1 * cards
        else:
            return cards # ask server how mamy cards played  

    def post_turn(prophet_decision=3): 
        calculate_points()
        """This function is called after each turn and it sets the updated # of points for each player. 
        prophet_decision = 1 if prophet made the RIGHT decision and player played the RIGHT card, 
        2 if prophet made the RIGHT decision and player played the WRONG card, 3 if prophet made the WRONG decision
             """
        #global other_player_points
        #global prophet_points
        #global prophet_player
    
        
      

        if self.prophet is None:
            return
        

        #access the the points of whatever player is prophet
        self.prophet += prophet_points
        print(other_player_points)

        if(prophet_decision == 3):
            self.prophet -= prophet_points
            reset_prophet()
        else:
            prophet_points += prophet_decision
            #other_player_points[prophet_player - 1] += prophet_decision


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



    def get_cards(self):
        return(self.cards)

    def get_points(self):
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