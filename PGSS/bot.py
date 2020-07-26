from game_player import Game
from game_player import Player
import random
class Bot():
    #create a list for similarities and one for differences
    #three levels: one card in hand, list of good cards and list of bad cards
    #Take in a list and compute similarities between card and list
    #this calls on another function that computes hte similarity of each of them
    
    # good_cards = []
    # bad_cards = []


    def __init__(self):
        self.good_cards = [(11,0),(11,1),(11,2),(11,3)]
        self.bad_cards = [(1,0),(2,0),(3,0),(4,0),(5,0),(6,1),(7,2),(8,3),(9,4),(10,5),(12,6)]
        self.bot_cards = [(2,0),(10,0),(3,0)]

        # print(good_cards())
        self.similarity_index = []
        

    # def get_good_cards(self,game):
    #     return game.good_cards
    
    # def get_bad_cards(self,game):
    #     return game.bad_cards
    
    def update_cards(self,game):
        self.good_cards = game.good_cards
        self.bad_cards = game.bad_cards

    #Remember to differentiate between face cards (J = 11, Q =12, K =13, A = 14)
    def determine_bot_cards(cards):
        self.bot_cards = cards
        
    def bot_turn(self,game):
        self.update_cards(game)
        self.get_similarity_all()
        # Returns the first card that has been played  if there has been one or finds the best card if there is none
        if 'pc' in self.similarity_index:
            return self.similarity_index['pc']
        # Checks to see if you have no cards that are similar cards to the correct cards
        # elif all(x <= 0 for x in similarity_index):
            # return 'no_similar_cards'
        # Checks for if all the similarity indexes are the same
        elif self.same_similarity_index() == 'True':
            # Chooses a random card to play
            card_choice = randint(1, self.similarity_index.len())
            return bot_cards[card_choice]
        else:
            best_card = self.determine_highest_similarity()
            return best_card

    def get_similarity_all(self): # game.good_cards, game.bad_cards
        for card in self.bot_cards:
            if(len(self.good_cards))==0:
                sim_good = 0
            else:
                sim_good = self.get_list_similarity(card, self.good_cards) # remember to change self to game.good_cards
            if(len(self.bad_cards))==0:
                sim_bad = 0
            else:
                 sim_bad = self.get_list_similarity(card, self.bad_cards) # remember to change self to game.bad_cards
            self.similarity_index.append(sim_good - sim_bad)
            
    
    def get_list_similarity(self, player_card, card_list):
        total = 0
        for index_card in card_list:
            total += self.get_similarity(player_card, index_card)
        if (len(card_list)>0):
            return total/len(card_list)
       
    
    def get_similarity(self, card_1, card_2):
        number = 0
        suit = 0
        even = 0
        odd = 0
       
        (number1, suit1) = card_1
        (number2, suit2) = card_2

        if number1 == number2:
            number = 1
        if suit1 == suit2:
            suit = 1
        if (number1 % 2 == 0) and (number2 % 2 == 0):
            even = 1
        elif (number1 % 2 >= 1) and (number2 % 2 >= 1):
            odd = 1
        return (number*2 + suit*3 + even + odd)
        
    def determine_highest_similarity(self):
        highest_similarity_number = 0
        highest_similarity_card = 0
        
        return self.bot_cards[self.similarity_index.index(max(self.similarity_index))]


    def same_similarity_index(self):
        # Takes the first number to compare to
        reference_number = self.similarity_index
        # Checks for a number that is different
        for number in self.similarity_index:
            if not(number == reference_number):
                # If there is a different similarity index
                return False
                break
        # If all similarity indexes are the same
        return True
    
    # def correct_cards():
    #     for number in self.similarity_index():
    #         if 

    # def calculate_confidence(Game.current_board):