from validate import Validate
from deck import Deck
from player import Player
from dealer import Dealer
from menu import Menu
from color import Color
class BlackJack:
    def blackjack(self):
        
        Color().color4("==========================\nBLACKJACK\n==========================")
        print("")

        num_players = Validate().inter("How many players will there be? " , "Please only enter a number")

        count = 1
        players = []
        while count <= num_players :
            hand = []
            name = Validate().string(f"Who is player {count}? ", "Please enter a valid name. ")
            player = Player(name,0,hand)
            players.append(player)
            count+= 1
        
        deck = Deck().create_deck()
        deck = Deck().shuffle_deck(deck)
        dealer_hand = []
        dealer = Dealer(deck,dealer_hand,0,0)
       
        BlackJack().deal(dealer,players)
      
        player21 = []
        winner = []
        bust = 0
        

        for player in players:
            if player.score > 21:
                players.remove(player)
        for player in players:
            if player.score > 21:
                bust +=1
                
       
        input("Press enter to start the Dealers turn")

        if len(players) == 0 or bust > 0 :
            Color().color4("All players busted , The dealer wins this game of Blackjack")
        

        else:
            highscore = 0
            for player in players:
                if player.score == 21:
                    player21.append(player)
                elif player.score < 21:
                    count = 0
                while count < len(players):
                    if highscore < players[count].score:
                        highscore = players[count].score
                    count +=1
            for player in players:
                if highscore == player.score:
                    winner.append(player)


            outcome = dealer.dealers_turn()
            if outcome == 1:
                if len(player21) > 0:
                    for player in player21:
                        print(f"{player.name} got a Blackjack {player.name} wins this game of Blackjack")
                elif len(player21)== 0:
                    for player in winner:
                        print(f"{player.name} is the closest to 21 with a hand of {player.score}")
                        print(f"{player.name} wins this game of Blackjack")
            elif outcome == 2:
                if len(player21) == 0:
                    Color().color4("No other player has 21, all players lose")
                else:
                    for player in player21:
                        print(f"{player.name} has 21 as well so they tie with the dealer")
            else:
                if len(player21) > 0:
                    for player in player21:
                        print(f"{player.name} wins this game of Blackjack")
                else:
                    for player in winner:
                        if player.score > dealer.score:
                            print(f"{player.name} got closer to 21 then the dealer with a hand of {player.score}")
                            print(f"{player.name} wins this game of Blackjack")
                        elif player.score == dealer.score:
                            print(f"{player.name} had the same score as the dealer")
                            Color().color2("This game is a tie")
                        else:
                            Color().color1(f"The dealer is the closest to 21 with a hand of {dealer.score}")
                            Color().color1(f"The dealer wins this game of Blackjack")
    

    def deal(self,dealer,players):
        Color().color1(f"The dealer draws {dealer.deck[0].display_card()}for himself ")
        dealer.hand.append(dealer.deck[0])
        Color().color1(f"the dealer draws a secound card and lays it face down.")
        dealer.hand.append(dealer.deck[1])

        dealer.deck.remove(dealer.deck[0])
        dealer.deck.remove(dealer.deck[0])
        
    
        for player in players:
            Color().color3(f"The dealer gives {player.name} {dealer.deck[0].display_card()}and {dealer.deck[1].display_card()}")
            player.deck.append(dealer.deck[0])
            player.deck.append(dealer.deck[1])
           
            dealer.deck.remove(dealer.deck[0])
            dealer.deck.remove(dealer.deck[0])

            BlackJack().card_check(dealer,player)
            input("press enter to start the next players turn.")
       

    def card_check(self,dealer,player):

        count = 0
        if len(player.deck) == 2:
            while count < len(player.deck):
                if player.deck[count].value ==1 :
                    player.ace_score = player.score +1
                    player.score += 11
                elif player.ace_score > 0:
                    player.score += player.deck[count].value
                    player.ace_score += player.deck[count].value
                elif player.deck[count].card_value > 1:
                    player.score += player.deck[count].value
                count += 1
            BlackJack().check21(dealer,player)
        else:
            if player.deck[-1].value ==1 :
                player.ace_score = player.score +1
                player.score += 11
            elif player.ace_score > 0:
                player.score += player.deck[-1].value
                player.ace_score += player.deck[-1].value
            elif player.deck[-1].card_value > 1:
                player.score += player.deck[-1].value
            BlackJack().check21(dealer,player)

    
    def check21(self,dealer,player):
        if player.score > 21:
            if player.ace_score > 0 and player.ace_score < 21 :
                player.score = player.ace_score
                player.ace_score = 0
                if player.score ==21:
                    Color().color3(f"{player.name} got 21")
                else:
                    Color().color2(f"Your hand is {player.score}")
                    BlackJack().play(dealer,player)
            else:
                Color().color2(f"Your hand is {player.score}")
                Color().color4("you have gone bust, you win nothing")
                
        elif player.score < 21:
            if player.ace_score > 0 :
                Color().color2(f"Your score is either {player.score} or {player.ace_score}")
                BlackJack().play(dealer,player)
            else:
                Color().color2(f"Your hand is {player.score}")
                BlackJack().play(dealer,player)
        elif player.score == 21:
            Color().color3(f"{player.name} got 21")



    def play(self,dealer,player):
        menu = ["Stand" , "Hit",]
        count =1
        for item in menu:
            print(f"{count}. {item}")
            count +=1
        while True:
            choice = input("What would you like to do? ")
            if choice == "1":
                Color().color2(f"{player.name} choose to stand at {player.score}")
                break
            elif choice == "2":
                BlackJack().hit(dealer,player)
                break
            else:
                Color().color4("Please enter a valid option.")
    
    def hit(self,dealer,player):
        Color().color3(f"The dealer gives {player.name} {dealer.deck[0].display_card()}")
        player.deck.append(dealer.deck[0])
        dealer.deck.remove(dealer.deck[0])
        BlackJack().card_check(dealer,player)


    
        
        

    




                


            
        
        

                    






    

        