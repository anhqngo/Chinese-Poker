suits = ['C', 'D', 'H', 'S']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
rank_value = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}

def isFour(hand):
    rankList = []
    for card in hand:
        rankList.append(rank_value[card.rank])
    s = set(rankList)
    if len(s) != 2:
        return False
    else:
        return rankList.count(list(set(rankList))[0]) == 4 or rankList.count(list(set(rankList))[0]) == 4

class Card(object):
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return self.rank + self.suit

    def __eq__(self, other):
        return self.rank == other.rank and self.suit == other.suit

hand2 = [Card('5', 'H'), Card('5', 'D'), Card(
            '5', 'C'), Card('5', 'S'), Card('4', 'H')]
print(isFour(hand2))