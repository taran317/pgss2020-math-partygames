class Game():
    prophet = None
    prophet_decision = 3
    current_board = { }
    # player1 = ""
    # list_of_players = []

    def __init__(self):
        player1 = Player()
        player2 = Player()
        player3 = Player()
        player4 = Player()
        
        # list_of_players.append(player1)
        

        # self.post_turn()
  
        

    def update_current_board(self,new_cards): #Gets the new cards from the server and upates them to the board
        self.current_board += new_cards
    
    def set_prophet(self,new_prophet):
        self.prophet = new_prophet
    

    def post_turn(self, valid, num_cards, prophet_decision = 3):
       #send information to bot class to analyze 
        
        # This function is called after each turn and it sets the updated # of points for each player. 
        # prophet_decision = 1 if prophet made the RIGHT decision and player played the RIGHT card, 
        # 2 if prophet made the RIGHT decision and player played the WRONG card, 3 if prophet made the WRONG decision"""
        #global other_player_points
        #global prophet_points
        #global prophet_player
 
        
        list_of_players[0].turn_points(most_cards())
        #self.player2.turn_points(most_cards())
        #self.player3.turn_points(most_cards())
        #self.player4.turn_points(most_cards())


        if self.prophet is None:
            calculate_cards(valid,num_cards)
            return

        #access the the points of whatever player is prophet
        self.prophet += prophet_points
      
        if(prophet_decision == 3):
            self.prophet -= prophet_points
            reset_prophet()
        else:
            prophet_points += prophet_decision
            #other_player_points[prophet_player - 1] += prophet_decision



        
    def most_cards():
        return max(player1.get_cards(), player2.get_cards(), player3.get_cards(), player4.get_cards())


class Player():
    # def set_prophet(prophet):
    #     global prophet_player
    #     prophet_player = prophet
    # def reset_prophet():
    #     global prophet_points
    #     prophet_points, prophet_player = 0, None
  

    def __init__(self):
        self.points = 0
        self.cards = 14
        self.list_of_good_cards = []
        self.list_of_bad_cards = []

    def turn(self, card, valid): # allow multiple cards
        if(valid):
            self.list_of_good_cards.append(card)
        else:
            self.list_of_bad_cards.append(card)

    def update_prophet():
        prophet = game.prophet

    def get_cards(self):
        return(self.cards)
        
    def get_points(self):
        return(self.points)

    def turn_points(most):
        #Remember to add 4 points to whoever has 0 cards at the end of the game
        self.points =  (most - self.cards)
    
    def calculate_cards(self, correct_play, cards_played): # ask server if correct play, delete parameters later if accessible from server directly
        if(correct_play):
             new_cards =  -1 * cards_played
        self.cards += new_cards
        # delete parameters later if accessible from server directly
        # make new_cards negative to ensure it works
        # new_cards = represents cards discarded or penalty
         # ask server how many cards played
        
        

    # def calculate_points(self, most):
    #     self.points = most - self.cards
    #     if (self.cards == 0):
    #         self.points += 4
    #     return self.points

   