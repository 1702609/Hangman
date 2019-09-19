import time
import tkinter as tk
from tkinter import font as tkfont
import random

import statManager
from PIL import ImageTk, Image
import threading

from GameGUI import GameGUI, populateUI


class WindowLauncher(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        global root
        root = self

        self.minsize(800, 600)
        self.grid_columnconfigure(0, weight=1)
        container = tk.Frame(self)
        container.grid_columnconfigure(0, weight=1)  # centers the GUI
        container.grid(row=0, column=0)

        self.frames = {}
        for F in (MainMenuUI, GameGUI):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("MainMenuUI")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


class MainMenuUI(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        global controller1
        controller1 = controller
        self.parent = parent
        title = tk.Label(self, text='Hangman Game', font=('Arial', 27))
        title.grid(row=0, column=0, pady=(8, 20))

        introduction = tk.Label(self, text='Please choose the following option:', bg='gold')
        introduction.grid(row=1, column=0, sticky='EW')

        start = tk.Button(self, text='Start the game', fg='red', command=gameLauncher)
        start.grid(row=2, column=0, pady=(16, 0))
        self.rowconfigure(1, weight=1)

        stats = tk.Button(self, text='View stats (coming soon)', fg='blue')
        stats.grid(row=3, column=0, pady=(8, 0))
        self.rowconfigure(2, weight=1)

        exitB = tk.Button(self, text='Exit', fg='green', bg='black', command=root.destroy)
        exitB.grid(row=4, column=0, pady=(8, 0))

def gameLauncher():
    populateUI()
    controller1.show_frame("GameGUI")



if __name__ == "__main__":
    app = WindowLauncher()
    app.mainloop()
