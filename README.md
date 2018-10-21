# Chinese Poker

**Instructions**
- Requirement: Python 2.7
- Run main file in the terminal: main_ChinesePoker.py
- Note: Best under Unix System. 
*(unicode characters might not work as well in Windows terminal)*
- When typing the cards you want to be in your hands, each card’s rank is followed by suit (case insensitive), and then a white space.
Ex: ‘9c 10s qh as’ (‘c’, ‘s’, ‘’d’, and ‘h’ stand for clubs, spade, diamonds and hearts respectively).
Ex: ‘JH 2D 3C 6S 8C’ (J, Q, K, A stand for Jack, Queen, King and Ace respectively)

**Rules for Chinese Poker**

- Chinese Poker is a card game based on poker hand rankings *(look up poker hand rankings if you are not familiar with them)*. 
- There are 2 players; each player receives 13 cards.
- Players then arrange their hand into three different groups: two five card poker hands, and one three card poker hand.
*Note: Straight and flushes don’t count in the three card hand, only high card, pairs and triples.*
- Once each player has set her hands, she compares each of the three hands with the opponent’s corresponding hands.
- Whether a player wins a hand is based on poker rankings. 
- Since there are three hands in total, the player who wins at least two out of three hands wins the game.
