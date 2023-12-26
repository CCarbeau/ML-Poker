class HandStrength:
    @staticmethod
    def detWin(hands,runout):
        handStr = {}
        #For each player left in the hand, add them to the handStr dictionary 
        #and assign them a hand strength 
        for key in hands:
            handStr[key] = HandStrength.handValue(hands[key],runout)

        #Find the lowest value(s) in handStr
        #handStr values:
        #1: Royal Flush
        #2: Straight Flush
        #3: Four of a kind 
        #4: Full House
        #5: Flush
        #6: Straight
        #7: Three of a kind
        #8: 2 pair
        #9: Pair
        #10: High card 
        ret=""
        dups=[]
        for key in handStr:
            if ret =="":
                ret=key
                dups.append(key)
            elif handStr[key]< handStr[ret]:
                ret=key
                dups=[]
                dups.append(key)
            elif handStr[key]==handStr[ret]:
                dups.append(key)
        #If no hands have the same hand strength, return the one with lowest hand strength
        if len(dups)==1:
            return ret
        dupsList=[]
        for x in dups:
            dupsList.append(hands[x])
        else:
            return HandStrength.tiebreak(dups,runout, handStr[dups[0]])
    
    @staticmethod
    def handValue(cards,runout):
        sevenCards=HandStrength.sortCards(cards,runout)
        if HandStrength.royalFlush(sevenCards):
            return 1
        elif HandStrength.straightFlush(sevenCards):
            return 2
        elif HandStrength.fourOfKind(sevenCards):
            return 3
        elif HandStrength.fullHouse(sevenCards):
            return 4
        elif HandStrength.flush(sevenCards):
            return 5
        elif HandStrength.straight(sevenCards):
            return 6
        elif HandStrength.threeOfKind(sevenCards):
            return 7
        elif HandStrength.twoPair(sevenCards):
            return 8
        elif HandStrength.pair(sevenCards):
            return 9
        else:
            return 10
    
    @staticmethod
    def tiebreak(dups,runout,handStr):
        bigList=[]
        for x in dups:
            bigList.append(HandStrength.sortCards(x,runout))
        
        #2 Straight Flushes
        if handStr == 2:
            suitedHands=[]
            for x in bigList:
                suitedHands.append(HandStrength.suitedList(x)[:5]) #looks at only the first 5 elements that suited returns
            i=0
            while i<5: 
                spotValue=[] #array that tracks the value of the current card within the hand
                j=0 #tracks the index of which player's hand we're looking at
                for x in bigList:
                    spotValue[j]=x[i][1] #assign each numerical value of the ith card of each 7 card sequence to an index in spotValue
                    j+=1

                max=-1
                dups2=[]
                elim=[] #track hands that are no longer being considered
                index=0 #track the index
                for x in spotValue:
                    if x > max:
                        for y in dups2:
                            elim.append((y,dups2[y]))
                        dups2=[]
                        max=x
                        dups2.append((max,index))
                    elif x == max:
                        dups2.append((max,index))
                    else:
                        elim.append((x,index))
                    index=index+1
                # Check if any ties remain 
                if len(dups2)==1:
                    return dups2[0][1]
                else: 
                    if i==4:
                        return -1 #Change to all indexes in dups2
                    else:
                        for x in elim:
                            bigList[elim[x]][i+1][1]=0 #sets the numerical value coordinate of the next card equal to 0
                i+=1
            return -1
             
        #Four of a kind 
        elif handStr == 3:
            fourOfKind=[] #tracks which card the 4 of a kind is of 
            i=0
            while i < len(bigList): #find the 4 of a kind and its value and set it equal to the hands index in fourOfKind
                                    #Ex: player 0's four of kind value is found at index 0 
                j=0
                while j < 4:
                    if bigList[i][j][1]==bigList[i][j+1][1]==bigList[i][j+2][1]==bigList[i][j+3][1]:
                        fourOfKind[i]=bigList[i][j][1]
                    j+=1
                i=i+1
            max=0
            dups2=[]
            elim=[] #track hands that are no longer being considered
            index=0 #track the index
            for x in fourOfKind:
                if x > max:
                    for y in dups2:
                        elim.append((y,dups2[y]))
                    dups2=[]
                    max=x
                    dups2.append((max,index))
                elif x == max:
                    dups2.append((max,index))
                else:
                    elim.append((x,index))
                index=index+1
            
            #Check if one hand has a higher value 4 of a kind then all the others, if so return it as winner
            if len(dups2)==1:
                return dups2[0][1]
            
            fourOfKindValue=dups2[0][1]
            # If there are still ties, check if one wins by high card and eliminate the ones that aren't in contention
            # Eliminate cards not in contention:
            for x in elim:
                bigList(elim[x])==HandStrength.sortCards(["00","00"],["00","00","00","00","00"])
            i=0
            while i < 5:
                spotValue=[] #array that tracks the value of each 7 card combo for a specific index within the 7
                j=0 #tracks the index of which player's hand we're looking at
                for x in bigList:
                    spotValue[j]=x[i][1] #assign each numerical value of the ith card of each 7 card sequence to an index in spotValue

                max=0
                dup3s=[]
                elim=[] #track hands that are no longer being considered
                index=0 #track the index
                for x in spotValue:
                    if x > max:
                        for y in dups3:
                            elim.append((y,dups3[y]))
                        dups3=[]
                        max=x
                        dups3.append((max,index))
                    elif x == max:
                        dups3.append((max,index))
                    else:
                        elim.append((x,index))
                    index=index+1
                # Check if one hand wins 
                if len(dups3)==1:
                    return dups3[0][1]
                
                #If the card is the same for multiple hands but not the 4 of a kind card, its a tie between those remaining players
                elif dups3[0][1]!=fourOfKindValue: 
                    return -1 #change this to the indexes found in dups
                i+=1
            return -1 #this should never be returned
        
        #2 Full Houses 
        elif handStr == 4:
            threeOfKind = []
            index=0
            #Find the value of the 3 of a kind in the full house
            for hand in bigList:
                i=0    
                while i < 5:
                    if (hand[i][1]==hand[i+1][1]==hand[i+2][1]):
                        threeOfKind[index]=hand[i][1]
                    i+=1
                index+=1
            
            #Find the value of the pair in the full house
            pairs=[]
            index=0
            for hand in bigList:
                i=0    
                while i < 6:
                    if (hand[i][1]==hand[i+1][1]):
                        pairs[index]=hand[i][1]
                    i+=1
                index+=1
            
            #Find the max value in 3 of a kind and its index
            max=0
            dups2=[]
            index=0 #track the index
            for value in threeOfKind:
                if value > max:
                    dups2=[]
                    max=value
                    dups2.append((max,index))
                elif value == max:
                    dups2.append((max,index))
                index=index+1
            if len(dups2)==1:
                return dups2[0][1]
            
            #Compare the value of the pairs of the hands in dups
            max=0
            dups3=[]
            index=0 #track the index
            for hand in dups2:
                if pairs[hand[1]] > max:
                    dups3=[]
                    max=value
                    dups3.append((max,index))
                elif value == max:
                    dups3.append((max,index))
                index=index+1
            if len(dups3)==1:
                return dups3[0][1]
            return -1 #Change to the index of the hands in dups3
        
        #Flushes
        elif handStr == 5: 
            suitedHands=[]
            for x in bigList:
                suitedHands.append(HandStrength.suitedList(x)[:5]) #looks at only the first 5 elements that suited returns
            i=0
            while i<5: 
                spotValue=[] #array that tracks the value of the current card within the hand
                j=0 #tracks the index of which player's hand we're looking at
                for x in bigList:
                    spotValue[j]=x[i][1] #assign each numerical value of the ith card of each 7 card sequence to an index in spotValue
                    j+=1

                max=-1
                dups2=[]
                elim=[] #track hands that are no longer being considered
                index=0 #track the index
                for x in spotValue:
                    if x > max:
                        for y in dups2:
                            elim.append((y,dups2[y]))
                        dups2=[]
                        max=x
                        dups2.append((max,index))
                    elif x == max:
                        dups2.append((max,index))
                    else:
                        elim.append((x,index))
                    index=index+1
                # Check if any ties remain 
                if len(dups2)==1:
                    return dups2[0][1]
                else: 
                    if i==4:
                        return -1 #Change to all indexes in dups2
                    else:
                        for x in elim:
                            bigList[elim[x]][i+1][1]=0 #sets the numerical value coordinate of the next card equal to 0
                i+=1
            return -1
            
        #Straights
        elif handStr == 6:
            #Find the value of the highest card in the straight
            straightValue=[] #Tracks value of highest card in the straight
            index=0
            for hand in bigList:
                i=0
                while i < 3: 
                    if(hand[i][1]==hand[i+1][1]+1==hand[i+2][1]+2==hand[i+3][1]+3==hand[i+4][1]+4):
                        straightValue[index]=hand[i][1]
                    elif (hand[1][1]==14 and hand[len(hand)-3][1]==5 and hand[len(hand)-2][1]==4 and hand[len(hand)-1][1]==3 and hand[len(hand)][1]==2):
                        straightValue[index]=14
                    i+=1
                index+=1
            
            #Find the index(es) of the max value(s) in straightValue:
            max=0
            dups2=[]
            index=0 #track the index
            for x in straightValue:
                if x > max:
                    dups2=[]
                    max=x
                    dups2.append((max,index))
                elif x == max:
                    dups2.append((max,index))
                index=index+1
            # Check if any ties remain 
            if len(dups2)==1:
                return dups2[0][1]
            else:
                return -1 #Change to indexes left in dups2 
        
        #3 of a kind
        elif handStr == 7: 
            threeOfKind = []
            index=0
            #Find the value of the 3 of a kind 
            for hand in bigList:
                i=0    
                while i < 5:
                    if (hand[i][1]==hand[i+1][1]==hand[i+2][1]):
                        threeOfKind[index]=hand[i][1]
                    i+=1
                index+=1
            
            #Find the index(es) of the max value(s) of the 3 of a kind
            max=0
            dups2=[]
            index=0 #track the index
            for x in threeOfKind:
                if x > max:
                    dups2=[]
                    max=x
                    dups2.append((max,index))
                elif x == max:
                    dups2.append((max,index))
                index=index+1
            # Check if any ties remain 
            if len(dups2)==1:
                return dups2[0][1]
            
            #Tiebreak w the remaining cards (This is a modified method of the code used to tiebreak high cards):
            i=0
            stop=0 #This integer keeps track of when the 2 other cards needed for the 5 card hand have been found
            while stop<3:
                spotValue=[] #array that tracks the value of each 7 card combo for a specific index within the 7
                j=0 #tracks the index of which player's hand we're looking at
                for x in dups2:
                    spotValue[j]=x[i][1] #assign each numerical value of the ith card of each 7 card sequence to an index in spotValue
                max=-1
                dups3=[]
                elim=[] #track hands that are no longer being considered
                index=0 #track the index
                for x in spotValue:
                    if x > max:
                        for y in dups3:
                            elim.append((y,dups3[y]))
                        dups3=[]
                        max=x
                        dups3.append((max,index))
                    elif x == max:
                        dups3.append((max,index))
                    else:
                        elim.append((x,index))
                    index=index+1
                # Check if any ties remain 
                if len(dups3)==1:
                    return dups3[0][1]
                
                # If they do, set the non-tied cards equal to a zeroed array 
                else:
                    #If the cards that tie are not the same value as the cards that make the 3 of a kind, they must take up 1 of the 2 
                    #remaining cards in the 5 card hand 
                    if dups3[0][1]!=dups2[0][1]:
                        stop+=1
                    if stop==2:
                        return -1 #Change to indexes in dups3 
                    for x in elim:
                        bigList[elim[x]][i+1][1]=0 #sets the numerical value coordinate of the next card equal to 0
                i+=1
        
        #2 pairs
        elif handStr == 8: 
            return -1
       
        #Pairs
        elif handStr == 9: 
            return -1
        
        #High Card
        else:
            i=0
            while i<5:
                spotValue=[] #array that tracks the value of each card at a spot in each hand 
                j=0 #tracks the index of which player's hand we're looking at
                for x in bigList:
                    spotValue[j]=x[i][1] #assign each numerical value of the ith card of each 7 card sequence to an index in spotValue

                max=0
                dups2=[]
                elim=[] #track hands that are no longer being considered
                index=0 #track the index
                for x in spotValue:
                    if x > max:
                        for y in dups2:
                            elim.append((y,dups2[y]))
                        dups2=[]
                        max=x
                        dups2.append((max,index))
                    elif x == max:
                        dups2.append((max,index))
                    else:
                        elim.append((x,index))
                    index=index+1
                # Check if any ties remain 
                if len(dups2)==1:
                    return dups2[0][1]
                
                # If they do, set the non-tied cards equal to a zeroed array 
                else:
                    if i==4:
                        return -1 #Change to indexes in dups2
                    for x in elim:
                        bigList[elim[x]][i+1][1]=0 #sets the numerical value coordinate of the next card equal to 0
                i+=1
    
    @staticmethod
    def sortCards(cards,runout):
        from operator import itemgetter
        #sort the 7 cards from highest to lowest and then by suit
        #Ace is high 
        #3=Spade
        #2=Club
        #1=Heart
        #0=Diamond
        sevenCards=cards+runout
        cardList=[]
        for card in sevenCards:
            i=0
            if card[-1]=="♠":
                i=3
            elif card[-1]=="♣":
                i=2
            elif card[-1]=="♥":
                i=1
            elif card[-1]=="♦":
                i=0
            elif card[-1]==0: #exception made to accommodate the tiebreak method
                i=-1
            if card[0:1]=="A":
                app=(card,14,i)
                cardList.append(app)
            elif card[0:1]=="K":
                app=(card,13,i)
                cardList.append(app)
            elif card[0:1]=="Q":
                app=(card,12,i)
                cardList.append(app)
            elif card[0:1]=="J":
                app=(card,11,i)
                cardList.append(app)
            else:
                app=(card,int(card[0:-1]),i)
                cardList.append(app)
        cardList=sorted(cardList, key=itemgetter(1,2), reverse=True)

        return cardList
   
    @staticmethod
    def royalFlush(cards):
        i=0
        while i < 3:
            if (cards[i][1]==cards[i+1][1]+1==cards[i+2][1]+2==cards[i+3][1]+3==cards[i+4][1]+4
            and cards[i][2]==cards[i+1][2]==cards[i+2][2]==cards[i+3][2]==cards[i+4][2] 
            and cards[i][1]==14):
                return True
            i=i+1
        return False
    
    @staticmethod
    def straightFlush(cards):
        suited=HandStrength.suitedList(cards) #returns a list of the cards with the most frequent suit of the 7 in cards
        i=0
        while i < len(suited)-4:
            if (suited[i][1]==suited[i+1][1]+1==suited[i+2][1]+2==suited[i+3][1]+3==suited[i+4][1]+4 
            or (suited[1][1]==14 and suited[len(suited)-4][1]==5 and suited[len(suited)-3][1]==4 and suited[len(suited)-2][1]==3 and suited[len(suited)-1][1]==2)):
                return True
            i=i+1
        return False
    
    @staticmethod
    def fourOfKind(cards):
        i=0
        while i < 4:
            if cards[i][1]==cards[i+1][1]==cards[i+2][1]==cards[i+3][1]:
                return True
            i=i+1
        return False
    
    @staticmethod
    def fullHouse(cards):
        i=0
        while i < 3:
            if (cards[i][1]==cards[i+1][1]==cards[i+2][1]):
                j=i+3
                while j < 6:
                    if cards[j][1]==cards[j+1][1]:
                        return True
                    j=j+1
            elif (cards[i][1]==cards[i+1][1]):
                j=i+2
                while j < 5:
                    if (cards[j][1]==cards[j+1][1]==cards[j+2][1]):
                        return True
                    j=j+1
            i=i+1
        return False
    
    @staticmethod
    def flush(cards):
        i=len(HandStrength.suitedList(cards))
        if i > 4:
            return True
        else:
            return False
    
    @staticmethod
    def straight(cards):
        noDups=HandStrength.removeDups(cards)
        i=0
        while i < len(noDups)-4:
            if((noDups[i][1]==noDups[i+1][1]+1==noDups[i+2][1]+2==noDups[i+3][1]+3==noDups[i+4][1]+4)
            or (noDups[1][1]==14 and noDups[len(noDups)-3][1]==5 and noDups[len(noDups)-2][1]==4 and noDups[len(noDups)-1][1]==3 and noDups[len(noDups)][1]==2)):
                return True
            i=i+1
        return False
    
    @staticmethod
    def threeOfKind(cards):
        i=0
        while i < 5:
            if cards[i][1]==cards[i+1][1]==cards[i+2][1]:
                return True
            i=i+1
        return False
    
    @staticmethod
    def twoPair(cards):
        i=0
        while i < 6:
            if cards[i][1]==cards[i+1][1]:
                j=i+2
                while j < 6:
                    if cards[j][1]==cards[j+1][1]:
                        return True
                    j=j+1
            i=i+1
        return False
    
    @staticmethod
    def pair(cards):
        i=0
        while i < 6:
            if cards[i][1]==cards[i+1][1]:
                return True
            i=i+1
        return False

    @staticmethod
    def removeDups(list):
        ret=[]
        i=0
        while i < len(list):
            j=0
            dup=False
            if len(ret)==0:
                ret.append(list[i])
            while j < len(ret):
                if(ret[j][1]==list[i][1]):
                    dup=True
                j=j+1
            if dup==False:
                    ret.append(list[i])
            i=i+1
        return ret
    
    @staticmethod
    def suitedList(cards):
        index=0 #tracks most prevalent suit
        max=0 #tracks amount of the suit marked by index
        i=0 #used to traverse cards
        j=0 #tracks which suit to track
        while j < 4:
            track=0 #Counts amount of a suit
            while i < len(cards):
                if cards[i][2]==j:
                    track=track+1
                i=i+1
            if track > max:
                index = j
                max=track
            j=j+1
        ret=[]
        k=0
        while k < len(cards):
            if cards[k][2]==index:
                ret.append(cards[k])
            k=k+1
        return ret