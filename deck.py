import random

class Deck(object):
    def __init__(self):
        self.cards = [1, 2, 3, 4, 5, 6, 7, 10, 11, 12] * 4
        self.shuffle_deck()
    
    def single_card(self):
        index = self.cards.index(self.random_card())
        return self.cards.pop(index)
        
    def random_card(self):
        return random.choice(self.cards)
        
    def shuffle_deck(self):
        return random.shuffle(self.cards)