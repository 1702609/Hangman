import threading
import tkinter as tk
import time

from PIL import ImageTk, Image

from GameEngine import GameEngine
from statManager import statManager



class GameGUI(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        global controller1
        controller1 = controller

        global hiddenWord
        hiddenWord = tk.Label(self, text="", font=(None, 20))
        hiddenWord.place(x=25, y=25, anchor="center")
        hiddenWord.grid(row=0, column=0)

        global entryFrame
        entryFrame = tk.Frame(self, bg='#fcedcc')
        tk.Label(entryFrame, text="Guess a Letter: ").grid(row=1, column=0)

        sv = tk.StringVar()
        sv.trace("w", lambda name, index, mode, sv=sv: self.limitCharacter(sv))

        global inputU
        inputU = tk.Entry(entryFrame, width=5, textvariable=sv)
        inputU.grid(row=1, column=1)

        global submitButton
        submitButton = tk.Button(entryFrame, text="Submit")
        submitButton.grid(row=1, column=2)
        submitButton.bind('<Button-1>', submitLetter)
        entryFrame.grid(row=1, column=0, pady=(8, 0))
        self.configure(bg='#fcedcc')
        self.grid(row=0, column=0)

        global canvas
        canvas = tk.Canvas(self, width=500, height=500, bg='red')

    def limitCharacter(self,sv):
        c = sv.get()[0:1]
        sv.set(c)

def populateUI():
    print("I shall populate the UI")
    global ge
    ge = GameEngine()
    hiddenWord.config(text=ge.getHiddenWord())
    print(ge.getChoosenWord())
    thread1 = threading.Thread(target=gameCompletionCheck)
    thread1.start()

def submitLetter( event):
    if submitButton['state'] == 'disabled':
        pass
    elif ge.isGuessCorrect(inputU.get()) == True:
        hiddenWord.config(text=ge.getUpdate(inputU.get()))
        inputU.delete(0, 'end')
    else:
        wrongGuess()

def wrongGuess():
    picID = ge.getNumberOfFails()
    img = ImageTk.PhotoImage(Image.open("img/pic" + str(picID) + ".png"))
    canvas.create_image(260, 400, image=img)
    canvas.grid(row=3, column=0, pady=20)
    inputU.delete(0, 'end')
    # The Label widget is a standard Tkinter widget used to display a text or image on the screen.
    controller1.mainloop()

def gameCompletionCheck():
    flag = True
    global resultText, backToMainMenu
    while flag:
        if "-" in hiddenWord.cget("text") and ge.getNumberOfFails() != 7:
            time.sleep(0.5)
        elif ge.getNumberOfFails() == 7:
            submitButton['state'] = 'disabled'
            flag = False
            resultText = tk.Label(entryFrame, text="You lose!")
            resultText.grid(row=2, column=1, pady=(8, 0))
            statManager.setWin(False)
        else:
            time.sleep(0.5)
            submitButton['state'] = 'disabled'
            flag = False
            resultText = tk.Label(entryFrame, text="You win!")
            resultText.grid(row=2, column=1, pady=(8, 0))
            statManager.setWin(True)
    statManager.updateStat()
    backToMainMenu = tk.Button(entryFrame, text="Main Menu", command=restart)
    backToMainMenu.grid(row=3, column=1, pady=(8, 0))
    print("The thread has been terminated")


def restart():
    print("The new word is "+ge.getChoosenWord())
    refresh()
    controller1.show_frame("MainMenuUI")

def refresh():
    ge.initialiseEngine()
    hiddenWord.config(text=" ")
    submitButton['state'] = 'active'
    canvas.grid_remove()
    resultText.destroy()
    backToMainMenu.destroy()