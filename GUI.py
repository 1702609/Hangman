from tkinter import *

import GameEngine

root = Tk()
launchFrame = Frame(root)


def gui_launcher():
    root.wm_geometry("500x500")
    introduction = Label(launchFrame, text='Please choose the following option:', bg='gold')
    introduction.pack(side="top", fill=BOTH, expand=True)
    start = Button(launchFrame, text='Start the game', fg='red')
    start.pack()
    start.bind('<Button-1>', startGame)
    stats = Button(launchFrame, text='View stats (coming soon)', fg='blue')
    stats.pack()
    exitB = Button(launchFrame, text='Exit', fg='green', bg='black')
    exitB.pack()
    launchFrame.pack(pady=20)
    root.mainloop()

def startGame(event):
    for widget in launchFrame.winfo_children():
        widget.destroy()
    chosenWord = GameEngine.wordpicker()
    hiddenWord = Label(launchFrame, text=GameEngine.getHiddenWord(chosenWord), font=(None, 20))
    hiddenWord.pack()
    print(chosenWord)
    launchFrame.pack()

gui_launcher()