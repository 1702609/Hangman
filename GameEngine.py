
class GameEngine:
    word = " "

    def __init__(self, choosenWord):
       self.word = choosenWord

    def getChoosenWord(self):
        return self.word

    def getHiddenWord(self):
        individual_list = []
        for ind in self.word: #converts words to string list
            individual_list.append(ind)
        dash = '-'
        list_of_dash = []
        for dash1 in individual_list: #converts list to dashes
            list_of_dash.append(dash)
        string_list_of_dash = ' '.join(list_of_dash)
        dashes_together = string_list_of_dash
        return dashes_together


    def user_input(self,uInput):
       return 0





