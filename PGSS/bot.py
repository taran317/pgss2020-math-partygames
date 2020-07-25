from game_player import Game
from game_player import Player
import random
class Bot():
    #create a list for similarities and one for differences
    #three levels: one card in hand, list of good cards and list of bad cards
    #Take in a list and compute similarities between card and list
    #this calls on another function that computes hte similarity of each of them

    bot_cards = []
    good_cards = []
    bad_cards = []
    similarity_index = []

#REmember to differentiate between face cards (J = 11, Q =12, K =13, A = 14)
    def determine_bot_cards(cards):
        self.bot_cards = cards
    def bot_turn(self):
        #Updates the confidence score each turn
        # self.confidence_score = calculate_confidence(get_simularity_all(bot_cards, good_cards, bad_cards), ):
        # if confidence_score >= 8:
        # possible_correct_cards = correct_cards()
        # if possible_correct_cards == 0:
        #     return all_bad_cards()
        # elif possible_correct_cards >= 1:
        #     if possible_correct_cards >= 4:
        #         return play_cards(bot_cards, current_cards, 4)
        #     elif possible_correct_cards == 0:
        #         return play_cards(bot_cards, current_cards, 1)
        #     else:
        #         return play_cards(bot_cards, current_cards, possible_correct_cards)
        # else:
        #     return play_cards(bot_cards, current_cards, 1)
        self.get_similarity_all(self, bot_cards, good_cards, bad_cards)
        # Returns the first card that has been played  if there has been one or finds the best card if there is none
        if 'pc' in similarity_index:
            return similarity_index['pc']
        # Checks to see if you have no cards that are similar cards to the correct cards
        elif all(x <= 0 for x in similarity_index):
            return 'no_similar_cards'
        # Checks for if all the similarity indexes are the same
        elif same_similarity_index(self) == 'True':
            # Chooses a random card to play
            card_choice = randint(1, similarity_index.len())
            return bot_cards[card_choice]
        else:
            best_card = self.determine_highest_similarity(self)
            return best_card

    def get_similarity_all(self, bot_cards, good_cards, bad_cards):
        for card in bot_cards:
            similarities = self.get_list_similarities(self, card, good_cards)
            differences = self.get_list_similarities(self, card, bad_cards)
            # Determines if the card is one that has already been played.
            if similarities == 6 & differences == 0:
                # Assignes pc (standing for played card) if the cars was already played
                self.similarity_index.append('pc')
            else:
                # Calculates the similarity index if not
                self.similarity_index.append(similarities - differences)
    def get_list_similarity(self, player_card, list):
        for index_card in list:
            return self.get_similarity(self, player_card, index_card)
    def get_similarity(self, card_1, card_2):
        number = 0
        suit = 0
        even = 0
        odd = 0
        (number1, suit1) = card
        (number2, suit2) = card
        if number1 == number2:
            number = 1
        if suit1 == suit2:
            suit = 1
        if (number1%2) == 0 & (number2%2) == 0:
            even = 1
        elif (number1%2) >= 1 & (number2%2) >= 1:
            odd = 1
        return number*2 + suit*3 + even + odd
    def determine_highest_similarity(self):
        highest_similarity_number = None
        highest_similarity_card = None
        for number in self.similarity_index:
            if number >> highest_similarity_number:
                highest_similarity_number = number
                highest_similarity_card = self.bot_cards(number)
        return highest_similarity_card
    def same_similarity_index(self):
        # Takes the first number to compare to
        reference_number = similarity_index
        # Checks for a number that is different
        for number in similarity_index():
            if number != reference_number():
                # If there is a different similarity index
                return False
                break
        # If all similarity indexes are the same
        return True
    
    # def correct_cards():
    #     for number in self.similarity_index():
    #         if 

    # def calculate_confidence(Game.current_board):


