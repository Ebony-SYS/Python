from tkinter import *
from tkinter import Tk, ttk
from PIL import Image, ImageTk

# ---------- ROOT ------------ ↓
preto = '#000'
branco = '#fff'
vermelho = '#cc1d4e'
amarelo = '#d1d420'
verde = '#59b356'
cinza = '#d9d9d9'
dark1 = '#101010'
dark2 = '#1e1e1e'
fonte = '#f7f7f5'

cores = ['#5588bb', '#66bbbb',
         '#99bb55', '#ee9944',
         '#444466', '#bb5555'
         ]
# ___________ ROOT ___________ ↑

# --------------- JANELA ----------------- ↓
janela = Tk()
janela.title('Ebony SyS | Despesas')
janela.geometry('900x700')
janela.configure(background=dark2)
janela.resizable(width=FALSE, height=FALSE)

style = ttk.Style(janela)
style.theme_use("clam")
# _______________ JANELA _________________ ↑

# -------------------------------------- FRAME'S -------------------------------------- ↓
frameTopo = Frame(janela, width=1043, height=50, bg=amarelo, relief='flat')
frameTopo.grid(row=0, column=0)

frameGrafico = Frame(janela, width=1043, height=361, bg=dark1, pady=20, relief='raised')
frameGrafico.grid(row=1, column=0, pady=1, padx=10, sticky=NSEW)

frameTabela = Frame(janela, width=1043, height=300, bg=dark1, relief='flat')
frameTabela.grid(row=2, column=0, pady=0, padx=10, sticky=NSEW)
# ______________________________________ FRAME'S ______________________________________ ↑

# --------------------------- POSICIONANDO LOGO NO FRAMETOPO -------------------------- ↓
imgLogo = Image.open('../assets/logo_cs_peq.png')
imgLogo = imgLogo.resize((45, 45))
imgLogo = ImageTk.PhotoImage(imgLogo)

labelLogo = Label(frameTopo, image=imgLogo, text='Ebony SyS', width=900, compound=LEFT,
                  padx=5, relief=RAISED, anchor=CENTER, font='Verdana 14 bold italic',
                  bg=dark1, fg=branco, borderwidth=0)
labelLogo.place(x=0, y=0)
# __________________________ POSICIONANDO LOGO NO FRAMETOPO __________________________ ↑




janela.mainloop()

