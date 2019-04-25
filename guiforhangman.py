from tkinter import *
import tkinter as tk
import random
words='feminist functionalist globalisation verstehen postmodernism durkheim parson murdock murray becker interactionism simulacra phenomenology'.split()

window=tk.Tk()

image=['''

   +---+
   |   |
       |
       |
       |
       |
=========''','''

   +---+
   |   |
   0   |
       |
       |
       |
=========''','''

   +---+
   |   |
   0   |
   |   |
       |
       |
=========''','''

   +---+
   |   |
   0   |
  /|   |
       |
       |
=========''','''

   +---+
   |   |
   0   |
  /|\  |
       |
       |
=========''','''

   +---+
   |   |
   0   |
  /|\  |
  /    |
       |
=========''','''

   +---+
   |   |
   0   |
  /|\  |
  / \  |
       |
=========''']


def wordpicker(words):
    return random.randint(0, len(words)-1) #it selects a number

def pieces(numberlist,words):
    return (words[numberlist]).lower() # from the "words" list, the word will be selected and they will all be lower case
    

def individual_character(selectedw):
    individual_list=[]
    for ind in selectedw:
        individual_list.append(ind) #The word gets broken down into individual alphabet and gets put into a list with the full list
    #print (individual_list)
    return individual_list

def word2dash(seperated_letters):
    global window 
    dash='-'
    list_of_dash=[]
    for dash1 in seperated_letters:
        dash1=dash
        list_of_dash.append(dash1)
    string_list_of_dash=''.join(list_of_dash)
    Label(window, text=string_list_of_dash).pack()
    dashes_together=string_list_of_dash
    return dashes_together

def user_input():
    global window
    #global seperated_letters
    while True:
        value=0
        global inputted_value
        user_answer=Entry(window, text="Click on a letter >")
        user_answer.bind('<Return>')
        user_answer.pack()
        user_answerT=user_answer.get()
        print(user_answer,'lololololololol')
        #if user_answer==''.join(seperated_letters):
            #IfitIsCorrect(dashes,inputted_value,image_code,Number_of_lives,seperated_letters)
        for position in inputted_value:
            if position==user_answerT:
                Label(window,text="You already typed the letter").pack()
                value=1
                break
            else:
                pass
        if value==1:
            continue
        for letter in user_answerT:
            if letter.isalpha()==False:
                Label(window,text="Invalid input").pack()
                continue
            else:
                inputted_value.append(user_answerT)
                #print (inputted_value)
        return user_answerT


def Verfication(seperated_letters,inputA,dashes,image):
    secondloop=0
    initialJoinedLetters=''.join(seperated_letters)
    number_of_goes=0 
    while True:
        if secondloop>=1:
            if str(dashes)==str(initialJoinedLetters):
                IfitIsCorrect(dashes,inputted_value,image_code,Number_of_lives,seperated_letters)
                main()
            else:
                inputA=user_input()
        else:
            pass
        right_count=0
        wrong_count=0
        number_of_loops=0
        for one in seperated_letters:
            number_of_loops +=1
            if inputA==one:
                right_count += 1
                dashes=Replacer(right_count,wrong_count,dashes,inputA,number_of_loops)
                continue
            else:
                wrong_count += 1
        if number_of_loops==len(seperated_letters):
            secondloop +=1
            if wrong_count>=1:
                if right_count==0:
                    Label(text="Wrong guess").pack()
                    IncorrectFunction(wrong_count,initialJoinedLetters,dashes,image)
                    pass 
                else:
                    print (dashes)
                    print("Correct")
                    continue
                
def Replacer(right_count,wrong_count,dashes,inputA,number_of_loops):
    dashes=list(dashes)
    dashes[(right_count+wrong_count)-1]=inputA
    dashes=''.join(dashes)
    return dashes

def IfitIsCorrect(dashes,inputted_value,image_code,Number_of_lives,seperated_letters):
    print("Well Done! You found the word!")

def IncorrectFunction(wrong_count,answer,dashes,image):
    global Number_of_lives, image_code
    Number_of_lives -=1
    image_code +=1
    #print(Number_of_lives,image_code)
    print (image[image_code])
    print (dashes)
    if Number_of_lives==0:
        print ('Loser! The answer is',answer,'\n')
        main()

def main():
    global Number_of_times_played
    if Number_of_times_played==-1:
        #response=gui_main()
        numberlist=wordpicker(words)
        selectedw=pieces(numberlist,words)
        seperated_letters=individual_character(selectedw)
        word2dash(seperated_letters) 
        inputA=user_input()
        #dashes=word2dash(seperated_letters)
        #Verfication(seperated_letters,inputA,dashes,image)
    else:
        global inputted_value,image_code,Number_of_lives
        del inputted_value[:]
        image_code=-1
        Number_of_lives=7
        numberlist=wordpicker(words)
        selectedw=pieces(numberlist,words)
        seperated_letters=individual_character(selectedw)
        word2dash(seperated_letters) 
        inputA=user_input()
        dashes=word2dash(seperated_letters)
        Verfication(seperated_letters,inputA,dashes,image)

class gui_main(Frame):
    def __init__(self,window):
        Frame.__init__(self,window)
        self.pack()
        self.button()
    def button(self):
        self.introduction=Label(self, text='Please choose the following option:',bg='gold')
        self.introduction.pack(side="top",fill=BOTH,expand=True)
        self.start=Button(self,text='Start the game',fg='red',command=self.del_button)
        self.start.pack()
        self.stats=Button(self,text='View stats (coming soon)',fg='blue')
        self.stats.pack()
        self.exitB=Button(self,text='Exit',fg='green',bg='black',command=exit)
        self.exitB.pack()
    def del_button(self):
        self.introduction.destroy()
        self.start.destroy()
        self.stats.destroy()
        self.exitB.destroy()
        self.main()
    def main(self):
        main()


Number_of_times_played=-1
inputted_value=[]
image_code=-1
Number_of_lives=7 

response=gui_main(window)
response.mainloop()

