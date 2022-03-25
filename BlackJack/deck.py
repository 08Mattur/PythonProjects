from random import shuffle
from collections import Counter

class deck(object):
    def __init__(self, deck_amount):
        self.cards = []
        self.deck_amount = deck_amount
        self.shuffle()


    def build_deck(self, deck_amount):
        deck = []
        for a in range(deck_amount):
            for b in range(9):
                for c in range(4):
                    deck.append(b+1)
            for b in range (4):
                for c in range(4):
                    deck.append(10)
        return deck

    def shuffle(self):
        self.cards = self.build_deck(self.deck_amount)
        shuffle(self.cards)
        
    def deck_size(self):
        return len(self.cards)

    def draw(self):
        c = self.cards.pop()
        return c

    def probability_of_card_needed(self, card):
        c = Counter(self.cards)
        total = 0
        for a in range(card):
            i = c.items()
            for items in i:
                if items[0] == a:
                    total += items[1]                        
        return (total / self.deck_size()) * 100
            
