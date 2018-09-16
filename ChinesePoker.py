suits_symbols = ['♠', '♦', '♥', '♣']

class Player(object):
    def __init__(self, name):
        self.name = name
        self.hand = [[],[],[]]
    
class Card(object):
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
    
class Move(object):
    pass

