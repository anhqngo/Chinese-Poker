# pylint: disable=W
from ChinesePoker import *
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

# poker_hand = {'Straight flush': 9, 'Four of a kind': 8, 'Full house': 7, 'Flush': 6,
#               'Straight': 5, 'Three of a kind': 4, 'Two pair': 3, 'One pair': 2, 'High card': 1}

def compareHands(hand1, hand2):
    score1 = getScore(hand1)
    score2 = getScore(hand2)

    rankList1 = []
    for card in hand1:
        rankList1.append(rank_value[card.rank])
        
    rankList2 = []
    for card in hand2:
        rankList2.append(rank_value[card.rank])
    
    if score1 > score2:
        print("hand1")
    elif score1 < score2:
        print("hand2")
    else:
        if max(rankList1) > max(rankList2):
            print("hand1")
        else:
            print("hand2")
    

def getScore(hand):
    if isStraightFlush(hand):
        return 9
    elif isFour(hand):
        return 8
    elif isFullHouse(hand):
        return 7
    elif isFlush(hand):
        return 6
    elif isStraight(hand):
        return 5
    elif isThree(hand):
        return 4
    elif isTwoPair(hand):
        return 3
    elif isPair(hand):
        return 2
    else:
        return 1

def isStraightFlush(hand):
    return isFlush(hand) and isStraight(hand)


def isFlush(hand):
    assert(len(hand) == 5)
    color = hand[0].suit
    for i in range(1, len(hand)):
        if hand[i].suit != color:
            return False
    return True


def isStraight(hand):
    assert(len(hand) == 5)
    num = []
    for card in hand:
        num.append(rank_value[card.rank])
    return (sorted(num) == list(range(min(num), max(num)+1))) or (set(num) == {14, 2, 3, 4, 5})


def isFour(hand):
    rankList = []
    for card in hand:
        rankList.append(rank_value[card.rank])
    s = set(rankList)
    if len(s) != 2:
        return False
    else:
        return rankList.count(list(set(rankList))[0]) == 4 or rankList.count(list(set(rankList))[1]) == 4


def isFullHouse(hand):
    rankList = []
    for card in hand:
        rankList.append(rank_value[card.rank])
    s = set(rankList)
    if len(s) != 2:
        return False
    else:
        """
        remember to deal with the cases when both hands are full house later
        """
        num1 = list(set(rankList))[0]
        num2 = list(set(rankList))[1]
        return rankList.count(num1) == 3 and rankList.count(num2) == 2


def isThree(hand):
    rankList = []
    for card in hand:
        rankList.append(rank_value[card.rank])
    l = list(set(rankList))
    for i in range(3):
        if rankList.count(l[i]) == 3:
            return True
    return False


def isTwoPair(hand):
    rankList = []
    for card in hand:
        rankList.append(rank_value[card.rank])
    s = set(rankList)
    return len(s) == 3


def isPair(hand):
    rankList = []
    for card in hand:
        rankList.append(rank_value[card.rank])
    s = set(rankList)
    return len(s) == 4


class UnitTest2(unittest.TestCase):
    def test_poker_hands(self):
        hand = [Card('6', 'H'), Card('2', 'H'), Card(
            '3', 'H'), Card('4', 'H'), Card('5', 'H')]
        self.assertEqual(isFlush(hand), True)
        self.assertEqual(isStraight(hand), True)

        hand2 = [Card('5', 'H'), Card('5', 'D'), Card(
            '5', 'C'), Card('5', 'S'), Card('4', 'H')]
        self.assertEqual(isFour(hand2), True)

    def test_compare(self):
        hand1 = [Card('6', 'H'), Card('2', 'H'), Card(
            '3', 'H'), Card('4', 'H'), Card('5', 'H')]

        hand2 = [Card('5', 'H'), Card('5', 'D'), Card(
            '5', 'C'), Card('5', 'S'), Card('4', 'H')]

        compareHands(hand1,hand2)

if __name__ == '__main__':
    #unittest.main()

    hand1 = [Card('6', 'H'), Card('2', 'C'), Card(
        '3', 'H'), Card('4', 'H'), Card('5', 'H')]

    hand2 = [Card('5', 'H'), Card('5', 'D'), Card(
        '5', 'C'), Card('5', 'S'), Card('4', 'H')]

    compareHands(hand1,hand2)
