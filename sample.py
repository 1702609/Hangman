import tkinter as tk

class PLG(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Enter the engine size (cc) below", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        vcmd = (self.register(self.onValidate), '%S')
        self.weight_entry = tk.Entry(self, validate='key', vcmd = vcmd)
        self.weight_entry.pack(pady = 10)
        tk.Button(self, text='Click here to display price', command=self.show_option).pack()
        self.text = tk.Text(self)
        self.text.pack(pady = 10)
        self.text.config(state='disabled')
        restart_button = tk.Button(self, text="Restart",
              command=self.restart)
        restart_button.pack()
        refresh_button = tk.Button(self, text="Refresh", command=self.refresh).pack()
        refresh_button.pack()

    def onValidate(self,S):
        if S in ['0','1','2', '3', '4', '5', '6', '7', '8', '9']:
            return True
        else:
            self.bell() # adds a sound effect to error
            self.text.delete(1.0, tk.END) # deletes the error message if valid entry provided
            self.text.insert(tk.END, "Invalid entry.  Please try again.") # displays an error message if a number not provided in entry widget
            return False

    def restart(self):
        self.refresh()
        self.show_frame("StartPage")

    def refresh(self):
        self.text.config(state='normal')
        self.weight_entry.delete(0,tk.END)
        self.text.delete("1.0", "end")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()

if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()