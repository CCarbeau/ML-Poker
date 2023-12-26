class Strategies:
    def __init__ (self, strat, hand, position, stack, street):
        self.strat=strat
        self.hand=hand
        self.position=position
        self.stack=stack
        self.street=street
    
    def GTO(hand,position,stack,street): 
        if (position == "UTG" or "SB" and street=="pre"):
            return "Fold"
        if (position == "Button" and street == "pre"):
            return "Call"
        if (position == "BB" and street == "pre"):
            return "Check"
    def Loose:

    def Tight:

