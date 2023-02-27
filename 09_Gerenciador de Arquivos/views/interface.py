from tkinter import *
from tkinter import Tk, StringVar
from tkinter import ttk as ttk
from tkinter import filedialog as fd
from tkinter import messagebox

import mixins.mixins
from mixins import *

# --------------------- criando janela
janela = Tk()
janela.geometry('700x360')
janela.title('Ebony SyS')
janela.resizable(width=FALSE, height=FALSE)

style = ttk.Style(janela)
style.theme_use("clam")

# --------------------- frame header
frame_header = Frame(janela, width=700, height=30, bg=mixins.dark2, relief='flat')
frame_header.grid(row=0, column=0)






# --------------------- frame main
frame_main = Frame(janela, width=700, height=300, bg=mixins.dark1)
frame_main.grid(row=1, column=0, sticky=NSEW)

# --------------------- frame footer
frame_footer = Frame(janela, width=700, height=30, bg=mixins.dark2)
frame_footer.grid(row=3, column=0)




janela.mainloop()