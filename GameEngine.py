
class GameEngine:
    word = " "
    wordArray = []
    dashArray = []
    failNo = 0

    def __init__(self, choosenWord):
        self.word = choosenWord
        for ind in self.word:  # converts words to string list
            self.wordArray.append(ind)

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
        self.dashArray = list_of_dash
        string_list_of_dash = ' '.join(list_of_dash) #converts dashes array back to string
        dashes_together = string_list_of_dash
        return dashes_together


    def isGuessCorrect(self, uInput):
        correctGuess = False
        for i in self.wordArray:
           if uInput == i:
               correctGuess = True
        if correctGuess == False:
            self.failNo +=1
        return correctGuess

    def getUpdate(self, uInput):
        index = 0
        for i in self.wordArray:
           if uInput == i:
               self.dashArray[index] = i
           index += 1
        string_list_of_dash = ' '.join(self.dashArray)
        return string_list_of_dash

    def getNumberOfFails(self):
        return self.failNo


