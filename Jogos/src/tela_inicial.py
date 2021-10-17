from tkinter import *

window = Tk()


class Aplication:

    def __init__(self):
        self.window = window
        self.firstWindow()
        self.frameFirstWindow()
        window.mainloop()

    def firstWindow(self):
        self.window.title("Ebony SYS")
        self.window.configure(background="#3a3b3c")
        self.window.geometry("700x700")
        self.window.resizable(True, True)
        self.window.maxsize(width=700, height=700)
        self.window.minsize(width=450, height=450)

    def frameFirstWindow(self):
        self.frame1 = Frame(self.window)
        self.frame1.place(relx=0, rely=0, relwidth=1, relheight=0.05)

        self.frame2 = Frame(self.window)
        self.frame2.place(relx=0.01, rely=0.06, relwidth=0.98, relheight=0.88)

        self.frame3 = Frame(self.window)
        self.frame3.place(relx=0, rely=0.95, relwidth=1, relheight=0.05)


Aplication()
