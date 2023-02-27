from tkinter import *
from tkinter import Tk, StringVar
from tkinter import ttk as ttk
from tkinter import filedialog as fd
from tkinter import messagebox
from PIL import Image, ImageTk
import mixins.mixins
from mixins import *

# --------------------- criando janela
janela = Tk()
janela.geometry('1080x720')
janela.title('Ebony SyS')
janela.resizable(width=FALSE, height=FALSE)
logo = PhotoImage(file=mixins.img_logo)
janela.iconphoto(False, logo)
style = ttk.Style(janela)
style.theme_use("clam")

# --------------------- frame header
frame_header = Frame(janela, width=1080, height=35, bg=mixins.dark2, relief='flat')
frame_header.grid(row=0, column=0)

icone_pasta = Image.open(mixins.icone_pasta)
icone_pasta = icone_pasta.resize((30, 30))
icone_pasta = ImageTk.PhotoImage(icone_pasta)

iconePasta = Label(frame_header, image=icone_pasta,
                   text='Gerenciador de Arquivos', width=1080, compound=LEFT,
                   padx=5, relief=RAISED, anchor=CENTER, font=mixins.fonte_principal,
                   bg=mixins.dark2, fg=mixins.cor_fonte_principal, borderwidth=0)
iconePasta.place(x=0, y=0)

# --------------------- frame main
frame_main = Frame(janela, width=1080, height=655, bg=mixins.dark1)
frame_main.grid(row=1, column=0, sticky=NSEW)

# --------------------- frame main/entrada
frame_entrada = Frame(frame_main, width=350, height=655, bg=mixins.dark2)
frame_entrada.place(x=0, y=0)
frame_entrada.lift()

label_escolher_pasta = Label(frame_entrada, text='Escolha uma pasta',
                             anchor=CENTER, relief='flat',
                             bg=mixins.dark2, fg=mixins.cor_fonte_principal,
                             font=mixins.fonte_secundaria)
label_escolher_pasta.place(x=87.5, y=30)




# --------------------- frame main/grafico
frame_grafico = Frame(frame_main, width=730, height=655, bg=mixins.dark1)
frame_grafico.place(x=351, y=0)





# --------------------- frame footer
frame_footer = Frame(janela, width=1080, height=30, bg=mixins.dark2)
frame_footer.grid(row=3, column=0)

janela.mainloop()
