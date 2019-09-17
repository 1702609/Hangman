import threading
import tkinter as tk
import time

from PIL import ImageTk, Image

from GameEngine import GameEngine
from statManager import statManager

words = 'short cold hot tall car'.split()

class GameGUI(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        global ge
        ge = GameEngine.getInstance()
        global hiddenWord
        hiddenWord = tk.Label(self, text=ge.getHiddenWord(), font=(None, 20))
        hiddenWord.place(x=25, y=25, anchor="center")
        hiddenWord.grid(row=0, column=0)
        print(ge.getChoosenWord())

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
        submitButton.bind('<Button-1>', self.submitLetter)
        entryFrame.grid(row=1, column=0, pady=(8, 0))
        self.configure(bg='#fcedcc')
        self.grid(row=0, column=0)

        global canvas
        canvas = tk.Canvas(self, width=500, height=500, bg='red')

        thread1 = threading.Thread(target=self.gameCompletionCheck)
        thread1.start()

    def submitLetter(self,event):
        if submitButton['state'] == 'disabled':
            pass
        elif ge.isGuessCorrect(inputU.get()) == True:
            hiddenWord.config(text=ge.getUpdate(inputU.get()))
            inputU.delete(0, 'end')
        else:
            self.wrongGuess()


    def wrongGuess(self):
        picID = ge.getNumberOfFails()
        img = ImageTk.PhotoImage(Image.open("img/pic" + str(picID) + ".png"))
        canvas.create_image(260, 400, image=img)
        canvas.grid(row=3, column=0, pady=20)
        inputU.delete(0, 'end')
        # The Label widget is a standard Tkinter widget used to display a text or image on the screen.
        self.mainloop()

    def limitCharacter(self,sv):
        c = sv.get()[0:1]
        sv.set(c)


    def gameCompletionCheck(self):
        flag = True
        while flag:
            if "-" in hiddenWord.cget("text") and ge.getNumberOfFails() != 7:
                time.sleep(0.5)
            elif ge.getNumberOfFails() == 7:
                submitButton['state'] = 'disabled'
                flag = False
                failMsg = tk.Label(entryFrame, text="You lose!")
                failMsg.grid(row=2, column=1, pady=(8, 0))
                statManager.setWin(False)
            else:
                time.sleep(0.5)
                submitButton['state'] = 'disabled'
                flag = False
                winMsg = tk.Label(entryFrame, text="You win!")
                winMsg.grid(row=2, column=1, pady=(8, 0))
                statManager.setWin(True)
        statManager.updateStat()
        backToMainMenu = tk.Button(entryFrame, text="Main Menu", command=self.restart)
        backToMainMenu.grid(row=3, column=1, pady=(8, 0))
        print("The thread has been terminated")

    def restart(self):
        self.refresh()
        ge.initialiseEngine()
        self.controller.show_frame("MainMenuUI")

    def refresh(self):
        hiddenWord.config(text="")

