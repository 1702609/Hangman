import time
import tkinter as tk
import random
from GameEngine import GameEngine
from PIL import ImageTk, Image
import threading

words = 'feminist functionalist globalisation verstehen postmodernism durkheim parson murdock murray becker ' \
            'interactionism simulacra phenomenology'.split()

root = tk.Tk()
root.grid_columnconfigure(0,weight=1)

launchFrame = tk.Frame(root, bg='#fcedcc', height=250, padx=25, pady = 10)
launchFrame.grid(row = 0, column=0,sticky='EW')
launchFrame.grid_columnconfigure(0, weight=1)
#bottomFrame = tk.Frame(root, bg='#fcedcc', width=500, height=500).pack(side = tk.BOTTOM)
canvas = tk.Canvas(root, width=500, height=500, bg = 'red')

def gui_launcher():
    root.wm_geometry("1000x600")
    introduction = tk.Label(launchFrame, text='Please choose the following option:', bg='gold')
    introduction.grid(row = 0, column =0, sticky='EW')
    start = tk.Button(launchFrame, text='Start the game', fg='red', pady= 10)
    start.grid(row = 1, column=0)
    start.bind('<Button-1>', startGame)
    stats = tk.Button(launchFrame, text='View stats (coming soon)', fg='blue')
    stats.grid(row = 2, column=0)
    exitB = tk.Button(launchFrame, text='Exit', fg='green', bg='black')
    exitB.grid(row = 3, column=0)

    ButtonFrame = tk.Frame(root)

    Button1 = tk.Button(ButtonFrame,
                         text="Delete").pack(side=tk.LEFT, padx=5, pady=5)
    Button2 = tk.Button(ButtonFrame,
                         text="Update").pack(side=tk.LEFT, padx=5, pady=5)
    Button3 = tk.Button(ButtonFrame,
                         text="Edit").pack(side=tk.LEFT, padx=5, pady=5)

    ButtonFrame.grid(row=2, column=0)

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
        widget.destroy()
    chosenWord = ge.getChoosenWord()
    global hiddenWord
    hiddenWord = tk.Label(launchFrame, text=ge.getHiddenWord(), font=(None, 20))
    hiddenWord.place(x=25, y=25, anchor="center")
    hiddenWord.pack()
    print(chosenWord)
    global entryFrame
    entryFrame=tk.Frame(root, bg='#fcedcc')
    tk.Label(entryFrame, text="Guess a Letter: ").pack(side="left")
    global inputU
    inputU = tk.Entry(entryFrame)
    inputU.pack(side="left")
    global submitButton
    submitButton = tk.Button(entryFrame, text="Submit")
    submitButton.pack(side="left")
    submitButton.bind('<Button-1>', submitLetter)
    entryFrame.pack(pady=20)
    launchFrame.configure(bg='#fcedcc')
    launchFrame.pack(fill=tk.X)

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
    canvas.pack()
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
    print("The thread has been terminated")

gui_launcher()