import random

class GameEngine:
    word = ""
    wordArray = []
    dashArray = []
    failNo = 0
    gameWin = False
    words = 'short cold hot tall car'.split()

    def __init__(self):
        self.word = self.pickaWord()
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

    def initialiseEngine(self):
        self.word = " "
        self.wordArray.clear()
        self.dashArray.clear()
        self.failNo = 0

    def pickaWord(self):
        num = random.randint(0, len(self.words) - 1)  # it selects a number
        return (self.words[num]).lower()