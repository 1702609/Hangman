import tkinter as tk
import random
from GameEngine import GameEngine
from PIL import ImageTk, Image

words = 'feminist functionalist globalisation verstehen postmodernism durkheim parson murdock murray becker ' \
            'interactionism simulacra phenomenology'.split()

root = tk.Tk()
launchFrame = tk.Frame(root, bg='#fcedcc', height=250, padx=5)
top_frame = tk.Frame(root, bg='cyan', width=500, height=50).pack()
#bottomFrame = tk.Frame(root, bg='#fcedcc', width=500, height=500).pack(side = tk.BOTTOM)
canvas = tk.Canvas(root, width=500, height=500, bg = 'red')

def gui_launcher():
    root.wm_geometry("1000x600")
    introduction = tk.Label(launchFrame, text='Please choose the following option:', bg='gold')
    introduction.pack(side="top", fill=tk.BOTH, expand=True)
    start = tk.Button(launchFrame, text='Start the game', fg='red')
    start.pack()
    start.bind('<Button-1>', startGame)
    stats = tk.Button(launchFrame, text='View stats (coming soon)', fg='blue')
    stats.pack()
    exitB = tk.Button(launchFrame, text='Exit', fg='green', bg='black')
    exitB.pack()
    launchFrame.pack(fill=tk.X)
    root.mainloop()

def getChoosenWord():
    num = random.randint(0, len(words) - 1)  # it selects a number
    return (words[num]).lower()

def startGame(event):
    global ge
    ge = GameEngine(getChoosenWord())
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
    submitButton = tk.Button(entryFrame, text="Submit")
    submitButton.pack(side="left")
    submitButton.bind('<Button-1>', submitLetter)
    entryFrame.pack(pady=20)
    launchFrame.configure(bg='#fcedcc')
    launchFrame.pack(fill=tk.X)

def submitLetter(event):
    if ge.isGuessCorrect(inputU.get()) == True:
        hiddenWord.config(text = ge.getUpdate(inputU.get()))
    else:
        picID = ge.getNumberOfFails()
        img = ImageTk.PhotoImage(Image.open("img/pic"+str(picID)+".png"))
        canvas.create_image(260, 400, image=img)
        canvas.pack()
        # The Label widget is a standard Tkinter widget used to display a text or image on the screen.
        root.mainloop()

gui_launcher()