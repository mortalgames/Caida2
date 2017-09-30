import random

class Deck(object):
    def __init__(self):
        self.cards = [1, 2, 3, 4, 5, 6, 7, 10, 11, 12] * 4
        self.shuffle_deck()
    
    def get_card(self):
        """
        Remove and return a single item from cards list
        @return int
        """
        return self.cards.pop(self.__get_index_from_random_card())

    def __get_index_from_random_card(self):
        """
        Get index from item in cards list
        @return int
        """
        return self.cards.index(self.get_random_card())
        
    def get_random_card(self):
        """
        Select a random card from cards list
        @return int
        """
        return random.choice(self.cards)

    def shuffle_deck(self):
        """ 
        Shuffle cards list
        @return list
        """
        return random.shuffle(self.cards)