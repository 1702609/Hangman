from tkinter import *
def main():
    pass

if __name__ == '__main__':
    main()

def callback(sv):
    c = sv.get()[0:1]
    print ("c=" , c)
    sv.set(c)

root = Tk()
sv = StringVar()
sv.trace("w", lambda name, index, mode, sv=sv: callback(sv))
e = Entry(root, textvariable=sv)
e.pack()
root.mainloop()