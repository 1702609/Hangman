import time
import tkinter as tk
import random
from GameEngine import GameEngine
from PIL import ImageTk, Image
import threading

words = 'short cold hot'.split()

root = tk.Tk()
root.minsize(800, 600)
root.grid_columnconfigure(0,weight=1)

def initialiseFrame():
    global launchFrame
    launchFrame = tk.Frame(root, bg='#fcedcc', height=250, padx=25, pady = 10)
    launchFrame.grid(row = 0, column=0,sticky='EW')
    launchFrame.grid_columnconfigure(0, weight=1)
    global canvas
    canvas = tk.Canvas(root, width=500, height=500, bg = 'red')

def gui_launcher():
    initialiseFrame()
    introduction = tk.Label(launchFrame, text='Please choose the following option:', bg='gold')
    introduction.grid(row = 0, column =0, sticky='EW')
    start = tk.Button(launchFrame, text='Start the game', fg='red')
    start.grid(row = 1, column=0, pady = (16,0))
    launchFrame.rowconfigure(1, weight=1)
    start.bind('<Button-1>', startGame)
    stats = tk.Button(launchFrame, text='View stats (coming soon)', fg='blue')
    stats.grid(row = 2, column=0, pady = (8,0))
    launchFrame.rowconfigure(2, weight=1)
    exitB = tk.Button(launchFrame, text='Exit', fg='green', bg='black')
    exitB.grid(row = 3, column=0,pady = (8,0))

    root.mainloop()

def getChoosenWord():
    num = random.randint(0, len(words) - 1)  # it selects a number
    return (words[num]).lower()

def startGame(event):
    global ge
    ge = GameEngine(getChoosenWord())
    guiForGame()
    thread1 = threading.Thread(target=isWordComplete)
    thread1.start()

def guiForGame():
    for widget in launchFrame.winfo_children():
        widget.destroy() #clears the window
    chosenWord = ge.getChoosenWord()
    global hiddenWord
    hiddenWord = tk.Label(launchFrame, text=ge.getHiddenWord(), font=(None, 20))
    hiddenWord.place(x=25, y=25, anchor="center")
    hiddenWord.grid(row = 0, column=0)
    print(chosenWord)
    global entryFrame
    entryFrame=tk.Frame(root, bg='#fcedcc')
    tk.Label(entryFrame, text="Guess a Letter: ").grid(row = 1, column=0)
    global inputU
    inputU = tk.Entry(entryFrame, width = 5)
    inputU.grid(row = 1, column=1)
    global submitButton
    submitButton = tk.Button(entryFrame, text="Submit")
    submitButton.grid(row = 1, column=2)
    submitButton.bind('<Button-1>', submitLetter)
    entryFrame.grid(row = 1, column=0, pady = (8,0))
    launchFrame.configure(bg='#fcedcc')
    launchFrame.grid(row = 0, column=0)

def submitLetter(event):
    if submitButton['state'] == 'disabled':
        pass
    elif ge.isGuessCorrect(inputU.get()) == True:
        hiddenWord.config(text = ge.getUpdate(inputU.get()))
    else:
        wrongGuess()

def wrongGuess():
    picID = ge.getNumberOfFails()
    img = ImageTk.PhotoImage(Image.open("img/pic" + str(picID) + ".png"))
    canvas.create_image(260, 400, image=img)
    canvas.grid(row = 3, column=0, pady = 20)
    # The Label widget is a standard Tkinter widget used to display a text or image on the screen.
    root.mainloop()


def isWordComplete():
    flag = True
    while flag:
        if "-" in hiddenWord.cget("text"):
            time.sleep(0.5)
        else:
            time.sleep(0.5)
            submitButton['state'] = 'disabled'
            flag = False
    backToMainMenu = tk.Button(entryFrame, text="Main Menu")
    backToMainMenu.bind('<Button-1>', restartGame)
    backToMainMenu.grid(row = 2, column=1, pady = (8,0))
    print("The thread has been terminated")

def restartGame(event):
    for widget in root.winfo_children():
        widget.destroy()
    ge.initialiseEngine()
    gui_launcher()


gui_launcher()