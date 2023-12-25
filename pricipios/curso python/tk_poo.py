import tkinter as tk

class App(tk.Frame):
    def __init__(self,master = None):
        super().__init__(master)
        self.master = master


root = tk.Tk()
root.wm_title("hola")
app =App(master=root)
app.mainloop()

