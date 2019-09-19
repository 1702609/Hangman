import tkinter as tk

import statManager


class StatGUI(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        global controller1
        controller1 = controller

        global numberOfWinsText
        numberOfWinsText = tk.Label(self, text="", font=(None, 20))
        numberOfWinsText.place(x=25, y=25, anchor="center")
        numberOfWinsText.grid(row=0, column=0)

        global numberOfLossText
        numberOfLossText = tk.Label(self, text="", font=(None, 20))
        numberOfLossText.place(x=25, y=25, anchor="center")
        numberOfLossText.grid(row=1, column=0)

        global mainMenuBtn
        mainMenuBtn = tk.Button(self, text="Main Menu", command=restart)
        mainMenuBtn.grid(row=2, column=0)


def populateUIStat():
    numberOfWins = str(statManager.statManager.getWin())
    numberOfLoss = str(statManager.statManager.getLoss())
    numberOfWinsText.config(text="Number of Wins: "+numberOfWins)
    numberOfLossText.config(text="Number of Loss: "+numberOfLoss)

def restart():
    refresh()
    controller1.show_frame("MainMenuUI")

def refresh():
    numberOfWinsText.config(text="")
    numberOfLossText.config(text="")
