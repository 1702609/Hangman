from tkinter import *
from tkinter import ttk

def Page():

    Profile = Tk()

    doesFrameWork = Frame(Profile)
    doesFrameWork.grid(row = 0, column=0)

    TreeSearchbar = Text(doesFrameWork, width=30, height=1, font="Arial 15")
    TreeSearchbar.grid(row=0, column=0, sticky=W, pady=5, columnspan=2)

    TreeSearchButton = ttk.Button(doesFrameWork, text="Search").grid(row=0, column=1, sticky=W)


    Tree = ttk.Treeview(doesFrameWork, height=20)
    Tree["columns"] = ("value1", "value2", "value3", "value4", "value5", "value6")
    Tree.column("#0", width=170)
    Tree.column("#1", width=180)
    Tree.column("#2", width=0)
    Tree.heading("#0", text="1")
    Tree.heading("#1", text="2")
    Tree.grid(row=1, column=0, sticky="nw", columnspan=2)

    Button1 = ttk.Button(doesFrameWork, text="Delete").grid(row=2, column=0, sticky=W, pady=12, padx=(20, 0))
    Button2 = ttk.Button(doesFrameWork, text="Update").grid(row=2, column=1, sticky=W)
    Button3 = ttk.Button(doesFrameWork, text="Edit").grid(row=2, column=2, sticky=W)

    Profile.mainloop()

Page()