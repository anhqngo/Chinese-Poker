
import random
import unittest

numPlayers = 2
# suits_symbols = ['♠', '♦', '♥', '♣']
# suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
suits = ['C', 'D', 'H', 'S']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
rank_value = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
              '8': 8, '9': 9, 'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
numCards = [5, 5, 3]

poker_hand = {'Straight flush': 9, 'Four of a kind': 8, 'Full house': 7, 'Flush': 6,
              'Straight': 5, 'Three of a kind': 4, 'Two pair': 3, 'One pair': 2, 'High card': 1}

class Player(object):
    def __init__(self, name, hand):
        self.name = name
        self.hand = hand
        self.groups = []


class Card(object):
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return self.rank + self.suit

    def __eq__(self, other):
        return self.rank == other.rank and self.suit == other.suit


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


def print_cards(hand):
    s = ""
    for card in hand:
        s += " " + str(card)
    return s


def get_card_from_input(user_input):
    deck = create_deck()
    if len(user_input) > 2:
        print("Not a valid input!")
        print("Proper input example: 2H or KC")
        return None
    for item in deck:
        if (item.rank == user_input[0]) and (item.suit == user_input[1]):
            return item
    return None


def print_groups(groups):
    newGroup = []
    for group in groups:
        newGroup.append(print_cards(group))
    return newGroup


class Game(object):
    def __init__(self):
        self.numPlayers = 2
        self.Players = []

        deck = create_deck()

        for _i in range(numPlayers):
            name = input("Enter the name of Player " + str(_i+1) + ": ")
            hand = dealHand(deck)
            self.Players.append(Player(name, hand))
        print('\n', self.Players[0].name, "will start first!")
        input("Press enter to start playing...\n")

    def play(self):
        print(self.Players[0].name + "'s cards are: ")
        print(print_cards(self.Players[0].hand))
        hand1 = self.Players[0].hand
        for _i in range(2):
            group = input(
                "Enter {} cards that you want to be in group {}: ".format(numCards[_i], _i+1))
            arr = group.split()
            # print(arr)
            arr2 = [get_card_from_input(i) for i in arr]
            # print(arr2)

            for card in arr2:
                for other in hand1:
                    if card == other:
                        hand1.remove(other)
            print("\nYour remaining cards are: " +
                  print_cards(self.Players[0].hand))
            self.Players[0].groups.append(arr2)
        self.Players[0].groups.append(hand1)
        print("\nYour three groups are: ")
        print(print_groups(self.Players[0].groups))


class UnitTest(unittest.TestCase):
    def test_create_deck(self):
        self.assertEqual(len(create_deck()), 52)

    def test_print_card(self):
        card = Card('4', 'Hearts')
        self.assertEqual(str(card), "4Hearts")

    def test_get_card_from_input(self):
        self.assertEqual(get_card_from_input("2H"), Card("2", "H"))

if __name__ == '__main__':
    #unittest.main()
    g = Game()
    g.play()


# class Move(object):
#     pass

# class Game(object):
#     def __init__(self, players):


# def main():

# if __name__ == "__main__":
#     main()
