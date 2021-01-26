from menu import Menu
from blackjack import BlackJack
from game import Game
import sys
class Game_menu:
   
    def game_menu(self):
       
        while True:
            menu_items = ["Blackjack" , "War" , "Exit"]
            menu = Menu(menu_items)
            menu.display_menu()
            choice = input("Which game would you like to play? ")
            if choice == "1":
                BlackJack().blackjack()
                self.end_game(1)
            elif choice == "2":
                Game().war()
                self.end_game(2)
            elif choice == "3":
                sys.exit(0)
            else :
                print("Please enter a valid option")
    def end_game(self,game):
        input("Press enter to continue")
        menu_item= ["Play Again", "Exit"]
        menu2 = Menu(menu_item)
        menu2.display_menu()
        while True:
            choice = input("Please choose an option ")
            if choice == "1":
                if game == 1:
                    BlackJack().blackjack()
                else:
                    Game().war()
                break
            elif choice == "2":
                break
            else:
                print("Please pick a valid option")



