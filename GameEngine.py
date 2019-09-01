
import random

words = 'feminist functionalist globalisation verstehen postmodernism durkheim parson murdock murray becker ' \
        'interactionism simulacra phenomenology'.split()

image = ['''

   +---+
   |   |
       |
       |
       |
       |
=========''', '''

   +---+
   |   |
   0   |
       |
       |
       |
=========''', '''

   +---+
   |   |
   0   |
   |   |
       |
       |
=========''', '''

   +---+
   |   |
   0   |
  /|   |
       |
       |
=========''', '''

   +---+
   |   |
   0   |
  /|\  |
       |
       |
=========''', '''

   +---+
   |   |
   0   |
  /|\  |
  /    |
       |
=========''', '''

   +---+
   |   |
   0   |
  /|\  |
  / \  |
       |
=========''']


def wordpicker():
    num = random.randint(0, len(words) - 1)  # it selects a number
    return (words[num]).lower()

def getHiddenWord(chossenWord):
    individual_list = []
    for ind in chossenWord: #converts words to string list
        individual_list.append(ind)
    dash = '-'
    list_of_dash = []
    for dash1 in individual_list: #converts list to dashes
        list_of_dash.append(dash)
    string_list_of_dash = ' '.join(list_of_dash)
    dashes_together = string_list_of_dash
    return dashes_together


def user_input():
    # global seperated_letters
    while True:
        value = 0
        global inputLetter
        user_answerT = user_answer.get()
        print('lololololololol')
        # if user_answer==''.join(seperated_letters):
        # IfitIsCorrect(dashes,inputted_value,image_code,Number_of_lives,seperated_letters)
        for position in inputLetter:
            if position == user_answerT:
                value = 1
                break
            else:
                pass
        if value == 1:
            continue
        for letter in user_answerT:
            if letter.isalpha() == False:
                continue
            else:
                inputLetter.append(user_answerT)
                # print (inputted_value)
        return user_answerT


def Verfication(seperated_letters, inputA, dashes, image):
    secondloop = 0
    initialJoinedLetters = ''.join(seperated_letters)
    number_of_goes = 0
    while True:
        if secondloop >= 1:
            if str(dashes) == str(initialJoinedLetters):
                IfitIsCorrect(dashes, inputLetter, image_code, numberOfLives, seperated_letters)
                main()
            else:
                inputA = user_input()
        else:
            pass
        right_count = 0
        wrong_count = 0
        number_of_loops = 0
        for one in seperated_letters:
            number_of_loops += 1
            if inputA == one:
                right_count += 1
                dashes = Replacer(right_count, wrong_count, dashes, inputA, number_of_loops)
                continue
            else:
                wrong_count += 1
        if number_of_loops == len(seperated_letters):
            secondloop += 1
            if wrong_count >= 1:
                if right_count == 0:
                    IncorrectFunction(wrong_count, initialJoinedLetters, dashes, image)
                    pass
                else:
                    print(dashes)
                    print("Correct")
                    continue


def Replacer(right_count, wrong_count, dashes, inputA, number_of_loops):
    dashes = list(dashes)
    dashes[(right_count + wrong_count) - 1] = inputA
    dashes = ''.join(dashes)
    return dashes


def IfitIsCorrect(dashes, inputted_value, image_code, Number_of_lives, seperated_letters):
    print("Well Done! You found the word!")


def IncorrectFunction(wrong_count, answer, dashes, image):
    global numberOfLives, image_code
    numberOfLives -= 1
    image_code += 1
    # print(Number_of_lives,image_code)
    print(image[image_code])
    print(dashes)
    if numberOfLives == 0:
        print('Loser! The answer is', answer, '\n')
        main()


def main():
    global playCount
    if playCount == -1:
        # response=gui_main()
        numberlist = wordpicker(words)
        selectedw = pieces(numberlist, words)
        seperated_letters = individual_character(selectedw)
        word2dash(seperated_letters)
        inputA = user_input()
        # dashes=word2dash(seperated_letters)
        # Verfication(seperated_letters,inputA,dashes,image)
    else:
        global inputLetter, image_code, numberOfLives
        del inputLetter[:]
        image_code = -1
        numberOfLives = 7
        numberlist = wordpicker(words)
        selectedw = pieces(numberlist, words)
        seperated_letters = individual_character(selectedw)
        word2dash(seperated_letters)
        inputA = user_input()
        dashes = word2dash(seperated_letters)
        Verfication(seperated_letters, inputA, dashes, image)



playCount = -1
inputLetter = []
image_code = -1
numberOfLives = 7

