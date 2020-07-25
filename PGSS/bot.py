from PGSS.game import Game
class Bot():
    #create a list for similarities and one for differences
    #three levels: one card in hand, list of good cards and list of bad cards
    #Take in a list and compute similarities between card and list
    #this calls on another function that computes hte similarity of each of them

    bot_cards = []
    good_cards = []
    bad_cards = []

#REmember to differentiate between face cards (J = 11, Q =12, K =13, A = 14)
    def bot_turn():
        #Updates the confidence score each turn
        self.confidence_score = calculate_confidence():
        if confidence_score >= 8:
            if possible_correct_cards == 0:
                return all_bad_cards()
            elif possible_correct_cards >= 1:
                if possible_correct_cards >= 4:
                    return play_cards(bot_cards, current_cards, 4)
                elif possible_correct_cards == 0:
                    return play_cards(bot_cards, current_cards, 1)
                else:
                    return play_cards(bot_cards, current_cards, possible_correct_cards)
        else:
            return play_cards(bot_cards, current_cards, 1)
    def get_similarity_all(bot_cards, good_cards, bad_cards):
        for card in bot_cards:
            get_list_similarities(card, good_cards)
            get_list_similarities(card, bad_cards)
    def get_list_similarity(player_card, list):
        for index_card in list:
            get_similarity(player_card, index_card)
    def get_similarity(card_1, card_2):
        number = 0
        suit = 0
        even = 0
        odd = 0
        (number1, suit1) = card
        (number2, suit2) = card
        if number1 == number2:
            number = 1
        if card_2[1] == card_2[1]:
            suit = 1
        if (card_1[0]%2) == (card_2[0]%2):
            if 
        

    def calculate_confidence(Game.current_board):


