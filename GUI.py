from tkinter import *

import GameEngine

root = Tk()
launchFrame = Frame(root, bg='#fcedcc', height=250, padx=5)

top_frame = Frame(root, bg='cyan', width=500, height=50).pack()

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
    launchFrame.pack(fill=X)
    root.mainloop()

def startGame(event):
    for widget in launchFrame.winfo_children():
        widget.destroy()
    chosenWord = GameEngine.wordpicker()
    hiddenWord = Label(launchFrame, text=GameEngine.getHiddenWord(chosenWord), font=(None, 20))
    hiddenWord.place(x=25, y=25, anchor="center")
    hiddenWord.pack()
    print(chosenWord)
    entryFrame=Frame(root, bg='#fcedcc')
    Label(entryFrame, text="Guess a Letter: ").pack(side="left")
    inputU = Entry(entryFrame)
    inputU.pack(side="left")
    submitButton = Button(entryFrame, text="Submit")
    submitButton.pack(side="left")
    entryFrame.pack(pady=20)
    launchFrame.configure(bg='#fcedcc')
    launchFrame.pack(fill=X)





gui_launcher()