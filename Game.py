import Deck
import HandStrength
def main(): 
    deck=Deck.Deck()
    Hands = deck.deal(deck.deck,2)
    runout=deck.runout(deck.deck)
    print(runout)
    i=1
    for key in Hands:
        print("Player "+str(i)+":",Hands[key]) 
        i=i+1
    print("Winner is:", HandStrength.HandStrength.detWin(Hands,runout))
    #print("Player 1:",HandStrength.HandStrength.handValue(Hands["Player1"],runout))
    #print("Player 2:",HandStrength.HandStrength.handValue(Hands["Player2"],runout))
    #print("Player 1:",HandStrength.HandStrength.sortCards(Hands["Player1"],runout))
    #print("Player 2:",HandStrength.HandStrength.sortCards(Hands["Player2"],runout))
if __name__ == "__main__":
    main()
