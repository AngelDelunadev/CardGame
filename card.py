class Card:

    def __init__(self,suit,card_value,value=1):
        self.suit = suit
        self.card_value = card_value
        self.value = value

    def display_card(self):
        card_suit = ""
        str_value = ""
        if self.suit == 1:
            card_suit = "Hearts"
        elif self.suit == 2:
            card_suit = "Diammonds"
        elif self.suit == 3:
            card_suit ="Clubs"
        else:
            card_suit = "Spades"
        
        if self.card_value <= 10 and self.card_value >= 2:
            str_value = str(self.card_value)
            self.value = self.card_value
        else:
            if self.card_value ==11:
                str_value = "Joker"
                self.value = 10
            elif self.card_value == 12:
                str_value = "Queen"
                self.value = 10
            elif self.card_value == 13:
                str_value = "King"
                self.value =10
            else:
                str_value = "Ace" 
                self.value= 1

        return (f"The {str_value} of {card_suit} ")







