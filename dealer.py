from card import Card
from deck import Deck
from color import Color
class Dealer:
    def __init__(self, deck, hand ,score , ace_score):
        self.deck = deck
        self.hand = hand
        self.score = score
        self.ace_score = ace_score

    def dealers_turn(self):
        Color().color1("It is now the dealers turn")
        Color().color1(f"The dealer has {self.hand[0].display_card()}and {self.hand[1].display_card()} ")
        self.deaker_check()
        if self.score > 21:
            return 1
        elif self.score == 21:
            return 2
        elif self.score < 21:
            return 3


    def deaker_check(self):
        count = 0
        if len(self.hand) == 2:
            while count < len(self.hand):
                if self.hand[count].value ==1 :
                    self.ace_score = self.score +1
                    self.score += 11
                elif self.ace_score > 0:
                    self.score += self.hand[count].value
                    self.ace_score += self.hand[count].value
                elif self.hand[count].card_value > 1:
                    self.score += self.hand[count].value
                count += 1
            self.check17()
                    
        else:
            if self.hand[-1].value ==1 :
                self.ace_score = self.score +1
                self.score += 11
            elif self.ace_score > 0:
                self.score += self.hand[-1].value
                self.ace_score += self.hand[-1].value
            elif self.hand[-1].card_value > 1:
                self.score += self.hand[-1].value
            self.check17()
    
    def check17(self):
        if self.score > 21:
            if self.ace_score > 0 and self.ace_score < 21 :
                self.score = self.ace_score
                self.ace_score = 0
                if self.score >= 17:
                    Color().color2(f"The dealers final hand is {self.score}")
                else:
                    Color().color2(f"The dealers hand is {self.score}")
                    Color().color1(f"The dealer gives himself {self.deck[0].display_card()}")
                    self.hand.append(self.deck[0])
                    self.deck.remove(self.deck[0])
                    self.deaker_check()
            else:
                Color().color2(f"The dealers hand is {self.score}")
                Color().color4("The dealer was busted")
        elif self.score == 21:
            Color().color1("the dealer has 21.")
        elif self.score >= 17:
            Color().color2(f"The dealers final hand is {self.score}")
        elif self.score < 17 :
            Color().color2(f"The dealers hand is {self.score}")
            Color().color1(f"The dealer gives himself {self.deck[0].display_card()}")
            self.hand.append(self.deck[0])
            self.deck.remove(self.deck[0])
            self.deaker_check()
  

       

                

