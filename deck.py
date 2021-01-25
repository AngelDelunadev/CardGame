from card import Card
import random
class Deck:
    
    def create_deck(self):
        deck = []
        suit = 0
        count = 1
        while suit < 4:
            while count<= 13:
                card = Card(suit,count)
                deck.append(card)
                count += 1
            suit += 1
            count = 1
        
        return deck

    def shuffle_deck(self, deck):
        new_deck = []
        while(len(deck) > 0):
            rand = random.randint(0,len(deck)-1)
            new_deck.append(deck[rand])
            deck.remove(deck[rand])
        
        return new_deck
    
    def divide_deck(self,deck):
        half1 = []
        half2 =[]
        pair = {}
        
        count = 0
        while(count < 52):
            if count > 25:
                half1.append(deck[count])
            else:
                half2.append(deck[count])
            count += 1
        pair["Half 1"] = half1
        pair["Half 2"] = half2
        return pair
        

    








            

