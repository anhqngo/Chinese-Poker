# -*- coding: utf-8 -*-
#!/usr/bin/python

import os
import random
import unittest
import pokertest
import pokertest_threeCards

suits_symbols = ['♠', '♦', '♥', '♣']
suits = ['C', 'D', 'H', 'S']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']


class Player(object):
    def __init__(self, name, hand):
        self.name = name
        self.hand = hand
        self.groups = []
        self.score = 0


class Card(object):
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return self.rank + self.suit

    def __eq__(self, other):
        return self.rank == other.rank and self.suit == other.suit


class Game(object):
    def __init__(self):
        self.numPlayers = 2
        self.Players = []

        deck = create_deck()

        for _i in range(self.numPlayers):
            name = raw_input("Enter the name of Player " + str(_i+1) + ": ")
            hand = dealHand(deck)
            self.Players.append(Player(name, hand))

    def play(self):
        for j in range(2):
            print("\nIt's {}'s turn now".format(self.Players[j].name))
            raw_input("Hit enter to continue...\n")

            print(self.Players[j].name + "'s cards are: ")
            hand = self.Players[j].hand

            print(beautify(print_cards(hand)))
            

            for _i in range(2):
                valid = False

                while valid == False:
                    group = raw_input(
                        "Enter {} cards that you want to be in group {}: ".format(5, _i+1))
                    inputArr = group.split()
                    cardArr = [get_card_from_input(i) for i in inputArr]
                    try:
                        assert(len(cardArr) == 5)
                        for card in cardArr:
                            assert(card in hand)
                            assert(cardArr.count(card) == 1)
                        valid = True
                    except:
                        print(
                            "\nThe program could not find in your hand one or more of the cards that you just provided")
                        print(
                            "This error is probably caused by a typo. Please try again.")
                        print(
                            "Remember, please type in 5 cards, separated by a white space.\n")
                        print("Again, your hand is: " +
                              beautify(print_cards(hand)))
                        continue

                    for card in cardArr:
                        for other in hand:
                            if card == other:
                                hand.remove(other)

                print("\nYour remaining cards are: " + beautify(print_cards(hand)))
                self.Players[j].groups.append(cardArr)

            self.Players[j].groups.append(hand)

            print("\nYour three groups are: ")
            for group in self.Players[j].groups:
                print(beautify(print_cards(group)))

            if j == 1:
                raw_input("Hit enter to see the results for the rounds!")
            else:
                raw_input("Hit enter to move to the other player...")

            os.system("cls") if os.name == 'nt' else os.system("clear") #clear

        winner = self.compare()

        print("The winner is: " + winner.name)
        print("Game over")

    def compare(self):
        for i in range(3):
            hand1 = print_cards(self.Players[0].groups[i])
            hand2 = print_cards(self.Players[1].groups[i])

            if i != 2: # the first two hands
                winnerIndex = pokertest.poker([hand1, hand2])
                if winnerIndex == 0:
                    self.Players[0].score += 1
                else:
                    self.Players[1].score += 1
            else: # last hand
                winnerIndex = pokertest_threeCards.poker([hand1, hand2])
                if winnerIndex == 0:
                    self.Players[0].score += 1
                elif winnerIndex == 1:
                    self.Players[1].score += 1

            ordinal = ['first', 'second', 'third']

            print("The cards for the {} round are: ".format(ordinal[i]))
            print(beautify(hand1) + "\tand\t" + beautify(hand2))
            if winnerIndex == None:
                print("It's a tie")
            else:
                print("The one whose hand is higher is " +
                      self.Players[winnerIndex].name + "\n")
            raw_input("Hit enter to see the next result")

        if self.Players[0].score > self.Players[1].score:
            return self.Players[0]
        else:
            return self.Players[1]


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
        s += str(card) + " "
    return s


def beautify(hand):
    handList = hand.split()
    beautify_string = ''
    for card in handList:
        if card[0] == 'T':
            rank = '10'
        else:
            rank = card[0]
        beautify_string += rank + suits_symbols[suits.index(card[1])] + " "
    return beautify_string.rstrip()


def get_card_from_input(user_input):
    deck = create_deck()
    user_input = user_input.upper().rstrip()

    if len(user_input) == 3 and user_input[:2] == '10':
        user_input = 'T' + user_input[-1]
    elif len(user_input) == 2:
        pass
    else:
        return None

    for item in deck:
        if (item.rank == user_input[0]) and (item.suit == user_input[1]):
            return item
    return None


class UnitTest(unittest.TestCase):
    def test_create_deck(self):
        self.assertEqual(len(create_deck()), 52)

    def test_print_card(self):
        card = Card('4', 'Hearts')
        self.assertEqual(str(card), "4Hearts")

    def test_get_card_from_input(self):
        self.assertEqual(get_card_from_input("2H"), Card("2", "H"))

    def test_beautify(self):
        self.assertEqual(beautify('2H 4C 9S TH'), '2♥ 4♠ 9♣ 10♥')

    def test_poker_rankings(self):
        self.assertEqual(pokertest.poker(
            ['8C TS KC 9H 4S', '8C AD 8D AC 9C']), 1)
        self.assertEqual(pokertest.poker(
            ['4H 4C 4D 3S 3D', '3H 3D 5C 5S 9S']), 0)

        self.assertEqual(pokertest_threeCards.poker(
            ['4H 4C 4D', '3H 3D 3C']), 0)
        self.assertEqual(pokertest_threeCards.poker(
            ['AC QC KD', '3H 3D 4C']), 1)
    
if __name__ == '__main__':
    i = 1  # Change it to 0 to test
    if i == 0:
        unittest.main()
    else:
        g = Game()
        g.play()
