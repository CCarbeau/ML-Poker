from random import choice
class Deck:
    def __init__(self):
        self.deck=["A♠", "A♥","A♦","A♣",
                   "K♠", "K♥","K♦","K♣", 
                   "Q♠","Q♥","Q♦","Q♣",
                   "J♠","J♥","J♦","J♣",
                   "10♠","10♥","10♦","10♣",
                   "9♠","9♥","9♦","9♣",
                   "8♠","8♥","8♦","8♣",
                   "7♠","7♥","7♦","7♣",
                   "6♠","6♥","6♦","6♣",
                   "5♠","5♥","5♦","5♣",
                   "4♠","4♥","4♦","4♣",
                   "3♠","3♥","3♦","3♣",
                   "2♠","2♥","2♦","2♣"]
    def runout(self,deck):
        c1=choice(deck)
        deck.remove(c1)
        c2=choice(deck)
        deck.remove(c2)
        c3=choice(deck)
        deck.remove(c3)
        c4=choice(deck)
        deck.remove(c4)
        c5=choice(deck)
        deck.remove(c5)
        return [c1,c2,c3,c4,c5]
    def deal(self,deck,players):
        Hands = {}
        for i in range(players):
            c1=choice(deck)
            deck.remove(c1)
            c2=choice(deck)
            deck.remove(c2)
            Hands["Player"+str((i+1))]=[c1,c2]
        return Hands
