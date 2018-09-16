import random

numPlayers = 2
suits_symbols = ['♠', '♦', '♥', '♣']
suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K']

class Player(object):
    def __init__(self, name, hand):
        self.name = name
        self.hand = hand

class Card(object):
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
    
    def __str__(self):
        """
        >>> card = Card('4', 'Hearts')
        >>> print(card)
        """
        return self.rank + ' ' + self.suit

def createDeck():
    """
    >>> assert(len(createDeck())==52)
    """
    Deck = []
    for s in suits:
        for r in ranks:
            card = Card(r,s)
            Deck.append(card)
    return Deck

def dealHand(deck):
    hand = []
    for _i in range(13):
        _j = random.choice(deck)
        deck.remove(_j)
        hand.append(_j)
    return hand

class Game(object):
    def __init__(self):
        self.numPlayers = 2
        self.Players = []
    
        deck = createDeck()

        for _i in range(numPlayers):
            name = input("Enter the name of Player " + str(_i+1) + ": ")
            hand = dealHand(deck)
            self.Players.append(Player(name,hand))

g=Game()
print(len(g.Players[1].hand))

# class Move(object):
#     pass

# class Game(object):
#     def __init__(self, players):


# def main():

# if __name__ == "__main__":
#     main()