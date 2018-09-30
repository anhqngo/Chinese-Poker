# pylint: disable=W
from ChinesePoker import Card
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


class PokerRankings(object):
    def __init__(self, hand):
        self.hand = hand

        self.rankList = []
        for card in self.hand:
            self.rankList.append(rank_value[card.rank])

        self.rankSet = set(self.rankList)

        self.highCard = 0 # the card used to determine the winner should two hands have the same score

    def isStraightFlush(self):
        self.highCard = max(self.rankList)
        return self.isFlush() and self.isStraight()

    def isFlush(self):
        self.highCard = max(self.rankList)
        firstColor = self.hand[0].suit
        # Check if the rest of the cards have the same color
        for i in range(1, len(self.hand)):
            if self.hand[i].suit != firstColor:
                return False
        return True

    def isStraight(self):
        self.highCard = max(self.rankList)
        return (sorted(self.rankList) == list(range(min(self.rankList), max(self.rankList)+1))) \
             or (set(self.rankList) == {14, 2, 3, 4, 5})

    def isFour(self):
        if len(self.rankSet) != 2:
            return False
        else:
            num1 = list(self.rankSet)[0]
            num2 = list(self.rankSet)[1]
            if self.rankList.count(num1) == 4:
                self.highCard = num1
                return True
            elif self.rankList.count(num2) == 4:
                self.highCard = num2
                return True
            else:
                return False

    def isFullHouse(self):
        if len(self.rankSet) != 2:
            return False
        else:
            """
            remember to deal with the cases when both hands are full house later
            """
            num1 = list(self.rankSet)[0]
            num2 = list(self.rankSet)[1]
            
            count_num1 = self.rankList.count(num1)
            count_num2 = self.rankList.count(num2)

            if count_num1 == 3 and count_num2 == 2:
                self.highCard = num1
                return True
            elif count_num1 == 2 and count_num2 == 3:
                self.highCard = num2
                return True
            else:
                return False

    def isThree(self):
        
        rank_shortList = list(self.rankSet)
        for i in range(3):
            if self.rankList.count(rank_shortList[i]) == 3:
                self.highCard = rank_shortList[i]
                return True
        return False

    def isTwoPair(self):
        
        return len(self.rankSet) == 3

    def isPair(self):
        return len(self.rankSet) == 4

    def getScore(self):
        if self.isStraightFlush():
            return 9
        elif self.isFour():
            return 8
        elif self.isFullHouse():
            return 7
        elif self.isFlush():
            return 6
        elif self.isStraight():
            return 5
        elif self.isThree():
            return 4
        elif self.isTwoPair():
            return 3
        elif self.isPair():
            return 2
        else:
            return 1


def compareHands(hand1, hand2):
    ranking1 = PokerRankings(hand1)
    ranking2 = PokerRankings(hand2)

    score1 = ranking1.getScore()
    score2 = ranking2.getScore()

    if score1 > score2:
        return (1,0)
    elif score1 < score2:
        return (0,1)
    else:
        if score1 == 7:     #handle full house separately
        if max(ranking1.rankList) > max(ranking1.rankList):
            print("hand1")
        else:
            print("hand2")


if __name__ == '__main__':
    # unittest.main()

    hand1 = [Card('6', 'H'), Card('2', 'C'), Card(
        '3', 'H'), Card('4', 'H'), Card('5', 'H')]

    hand2 = [Card('5', 'H'), Card('5', 'D'), Card(
        '5', 'C'), Card('5', 'S'), Card('4', 'H')]

    compareHands(hand1, hand2)
