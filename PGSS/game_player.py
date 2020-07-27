class Game():
    prophet = None
    prophet_decision = 3
    current_board = { }
    prophet_points = 0
   
    #players = []

    def __init__(self):
      
        player1 = Player()
        player2 = Player()
        player3 = Player()
        player4 = Player() 
        self.players = [player1,player2,player3,player4]
        self.good_cards = []
        self.bad_cards = []
        self.recent_valid = None

        
    def __str__(self):
        i = 1
        output = ""
        for num in self.players:
            output += "Player "+ str(i) + " :\tCards: "+ str(num.get_cards())+ "\tPoints: "+ str(num.get_points()) + "\n"
            i += 1
        output += 'Good Cards: ' + str(self.good_cards) + '\nBad Cards: ' + str(self.bad_cards) + '\n'
        return(output)
    
    def good_cards(self):
        return self.good_cards
    def bad_cards(self):
        return self.bad_cards

    def update_current_board(self,new_cards): #Gets the new cards from the server and upates them to the board
        self.current_board += new_cards
    
    def set_prophet(self,new_prophet):
        self.prophet = new_prophet
    
    def turn(self, player, card, valid): # allow multiple cards
            self.recent_valid = valid
            if(valid):
                self.good_cards.extend(card)
            else:
                self.bad_cards.extend(card)
            self.post_turn(player, valid, len(card))


    def post_turn(self, player, valid, num_cards, prophet_decision = 3):
       #send information to bot class to analyze 
        
        # This function is called after each turn and it sets the updated # of points for each player. 
        # prophet_decision = 1 if prophet made the RIGHT decision and player played the RIGHT card, 
        # 2 if prophet made the RIGHT decision and player played the WRONG card, 3 if prophet made the WRONG decision"""
        #global other_player_points
        #global prophet_points
        #global prophet_player
            
        player.calculate_cards(valid,num_cards)
        for player in self.players:
            player.turn_points(self.most_cards())

       #prophet points would clear if run after each turn?
        if self.prophet is not None:
            if(prophet_decision == 3):
                self.prophet_points = 0
                self.prophet = None
            else:
                self.prophet_points += prophet_decision
                self.prophet.add_points_to_prophet(self.prophet_points)
                
    def most_cards(self):
        return max(self.players[0].get_cards(), self.players[1].get_cards(), self.players[2].get_cards(), self.players[3].get_cards())


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


    def update_prophet(self):
        prophet = game.prophet

    def add_points_to_prophet(self,more_points):
        self.points += more_points


    def get_cards(self):
        return(self.cards)
        
    def get_points(self):
        return(self.points)

    def turn_points(self, most):
        #Remember to add 4 points to whoever has 0 cards at the end of the game
        self.points =  (most - self.cards)
    
    def calculate_cards(self, correct_play, cards_played): # ask server if correct play, delete parameters later if accessible from server directly
        new_cards = cards_played
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