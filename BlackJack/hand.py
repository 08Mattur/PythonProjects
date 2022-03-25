
from pickle import FALSE


class hand(object):
    doubled = False
    
    def __init__(self):
        self.cards = []
    
    def add_card(self, c):
        self.cards.append(c)

    def busted(self):
        return self.value() > 21            

    def blackjack(self):
        if len(self.cards) == 2:
            if self.cards[0] == 1 or self.cards[1] == 1:
                if self.cards[0] == 10 or self.cards[1] == 10:
                    return True
        return False

    def value(self):
        return sum(self.cards)

    def soft(self):
        return 1 in self.cards and self.value() <= 11

    def soft_value(self):
        v = self.value()
        if self.soft():
            v += 10
        return v

    def final_value(self):
        if self.soft():
            return self.soft_value()
        return self.value()

    def __str__(self):
        r = ''
        for card in self.cards:
            r += str(card) + ', '
        return r
        

    
            

        
            
                
            