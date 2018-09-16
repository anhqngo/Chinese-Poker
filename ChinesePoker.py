import random
import unittest
import deuces

numPlayers = 2
# suits_symbols = ['♠', '♦', '♥', '♣']
# suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
suits = ['C', 'D', 'H', 'S']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']


class Player(object):
    def __init__(self, name, hand):
        self.name = name
        self.hand = hand


class Card(object):
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return self.rank + self.suit


def create_deck():
    Deck = []
    for s in suits:
        for r in ranks:
            card = Card(r, s)
            Deck.append(card)
    return Deck


def dealHand(deck):
    hand = []
    for _i in range(13):
        _j = random.choice(deck)
        deck.remove(_j)
        hand.append(_j)
    return hand


def print_cards(deck):
    s = ""
    for card in deck:
        s += " " + str(card)
    return s


def get_card_from_input(deck, user_input):
    if len(user_input) > 2:
        print("Not a valid input!")
        print("Proper input example: 2H or KC")
        return None
    for item in deck:
        if (item.rank == user_input[0]) and (item.suit == user_input[1]):
            return item
    return None


class Game(object):
    def __init__(self):
        self.numPlayers = 2
        self.Players = []

        deck = create_deck()

        for _i in range(numPlayers):
            name = input("Enter the name of Player " + str(_i+1) + ": ")
            hand = dealHand(deck)
            self.Players.append(Player(name, hand))


class UnitTest(unittest.TestCase):
    def test_create_deck(self):
        self.assertEqual(len(create_deck()), 52)

    def test_print_card(self):
        card = Card('4', 'Hearts')
        self.assertEqual(str(card), "4Hearts")


if __name__ == '__main__':
    unittest.main()


# class Move(object):
#     pass

# class Game(object):
#     def __init__(self, players):


# def main():

# if __name__ == "__main__":
#     main()
