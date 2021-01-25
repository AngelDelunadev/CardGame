class Menu:

    def __init__(self,menu):
        self.menu = menu

    def display_menu(self):
        count = 1
        for item in self.menu:
            print(f"{count}. {item}")
            count += 1
        print("")

