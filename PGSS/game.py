from PGSS.player import player

class Game():
    prophet = None
    prophet_decision = 3
    current_board = { }

    def update_current_board(new_cards): #Gets the new cards from the server and upates them to the board
        self.current_board =+ new_cards
    
    def set_prophet(self,prophet):
        self.prophet = prophet

    def __init__(self):
        player1 = Player()
        player2 = Player()
        player3 = Player()
        player4 = Player() 
    
    def penalties(correct_play, cards): # ask server if correct play, delete parameters later if accessible from server directly
        if(correct_play):
            return -1 * cards
        else:
            return cards # ask server how mamy cards played  

    def post_turn(prophet_decision=3): 
        """ This function is called after each turn and it sets the updated # of points for each player. 
        prophet_decision = 1 if prophet made the RIGHT decision and player played the RIGHT card, 
        2 if prophet made the RIGHT decision and player played the WRONG card, 3 if prophet made the WRONG decision"""
        #global other_player_points
        #global prophet_points
        #global prophet_player
    
        other_player_points = turn_points()
        if self.prophet is None:
            break

        #access the the points of whatever player is prophet
        self.prophet += prophet_points
        print(other_player_points)

        if(prophet_decision == 3):
            self.prophet -= prophet_points
            reset_prophet()
        else:
            prophet_points += prophet_decision
            #other_player_points[prophet_player - 1] += prophet_decision