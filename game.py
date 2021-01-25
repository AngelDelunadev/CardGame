from deck import Deck
from card import Card
from colorama import Fore, Back , Style
from validate import Validate
from player import Player
from color import Color
import sys
class Game():

    def war(self):
        cards = Deck().create_deck()
        Color().color4("=====================  \nWelcome to War! \n===================== ")

        name1 = Validate().string(Fore.BLUE + "Who is Player 1? ","Please don't leave this empty , or use only numbers")

        name2 = Validate().string(Fore.YELLOW + "Who is Player 2? ","Please don't leave this empty , or use only numbers")
        
        pair = {}
        cards = Deck().shuffle_deck(cards)
        pair = Deck().divide_deck(cards)

        player1 = Player(name1,0,pair["Half 1"])
        player2 = Player(name2,0,pair["Half 2"])

        Game().play(player1,player2)


    def play(self,player1,player2):
        Color().color3(f"We've got two players. {player1.name} and {player2.name}")

        while len(player1.deck) > 0:
            choice = input("Shall we play a round of War (y/n) ")
            choice = choice.lower()
            if choice == "y":
                Game().round(player1,player2)
            elif choice == "n":
                sys.exit(0)
            else:
                print("please enter y or n ")
        Game().end_game(player1,player2)

    def round(self,player1,player2):
        P1card = player1.deck[0].display_card()
        Color().color1(f"{player1.name} has the {P1card}")

        P2card = player2.deck[0].display_card()
        Color().color2(f"{player2.name} has the {P2card}")

        if player1.deck[0].card_value > player2.deck[0].card_value:
            Color().color1(f"{player1.name.upper()} WINS THIS ROUND ")
            player1.score += 1
        elif player1.deck[0].card_value < player2.deck[0].card_value:
            Color().color2(f"{player2.name.upper()} WINS THIS ROUND" )
            player2.score += 1
        elif player1.deck[0].card_value == player2.deck[0].card_value:
            Color().color3(f"TIE! , NOBODY WINS")

        player1.deck.remove(player1.deck[0])
        player2.deck.remove(player2.deck[0])
        Game().display_score(player1,player2)
        

    def display_score(self,player1,player2):
        Color().color4("****************************")
        Color().color1(f"{player1.name}: {player1.score}")
        Color().color2(f"{player2.name}: {player2.score}")
        print(f"Each player has {len(player1.deck)} cards left in their deck ")
        Color().color4("****************************")

    def end_game(self,player1,player2):
        print()
        print("End of game")
        Color().color4("=========================\nFINAL SCORE")
        self.display_score(player1,player2)
        if player1.score > player2.score:
            Color().color1(f"{player1.name.upper()} WINS THE GAME OF WAR!")
        elif player1.score < player2.score:
            Color().color2(f"{player2.name.upper()} WINS THE GAME OF WAR!")
        elif player1.score == player2.score:
            Color().color3("THIS GAME WAS TIE! NOBODY WINS")
        
        
        





            
    


       



