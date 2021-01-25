from color import Color
class Validate():

    def string(self,question,text):
        user_input = input(question)
        while user_input.isnumeric() or not user_input:
            Color().color4(text)
            user_input = input(question)
        return user_input

    def inter(self,question,text):
        user_input = input(question)
        while not user_input.isnumeric():
            Color().color4(text)
            user_input = input(question)
        return int(user_input)
