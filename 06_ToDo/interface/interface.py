from tkinter import *
from PIL import Image, ImageTk

preto = '#000'
branco = '#fff'
vermelho = '#ff0808'
vermelhoEsc = '#8c0715'
amarelo = '#f7f702'
amareloEsc = '#979908'
verde = '#0bf702'
verdeEsc = '#064f04'
azul = '#02c0fa'
azulEsc = '#012b4f'


cinza = '#d9d9d9'
dark1 = '#101010'
dark2 = '#1e1e1e'
fonte = '#f7f7f5'

# ------------------ CRIANDO JANELA ------------------ ↓
janela = Tk()
janela.resizable(width=FALSE, height=FALSE)
janela.geometry('750x400')
janela.title('Ebony Sys | Leonardo Alves → To-Do')
janela.configure(background=dark1)
# ------------------ CRIANDO JANELA ------------------ ↑

# -------------------------------- CRIANDO FRAMES -------------------------------- ↓
frameTopo = Frame(janela, width=750, height=34, bg=verde, relief='flat')
frameTopo.grid(row=0, column=0, columnspan=2, sticky=NSEW)

frameEsqueda = Frame(janela, width=420, height=400, bg=dark1, relief='flat')
frameEsqueda.grid(row=1, column=0, sticky=NSEW)

frameDireita = Frame(janela, width=330, height=400, bg=dark1, relief='flat')
frameDireita.grid(row=1, column=1, sticky=NSEW, padx=10)

# Dividindo frameEsqueda em 2 partes
frameEsqueda1 = Frame(frameEsqueda, width=420, height=50, bg=dark1, relief='flat')
frameEsqueda1.grid(row=0, column=0, sticky=NSEW)

frameEsqueda2 = Frame(frameEsqueda, width=420, height=350, bg=dark1, relief='flat')
frameEsqueda2.grid(row=1, column=0, sticky=NSEW)

# -------------------------------- CRIANDO FRAMES -------------------------------- ↑
# --------------------------- POSICIONANDO LOGO NO FRAMETOPO -------------------------- ↓

imgLogo = Image.open('../assets/logo_cs_peq.png')
imgLogo = imgLogo.resize((30, 30))
imgLogo = ImageTk.PhotoImage(imgLogo)

labelLogo = Label(frameTopo, image=imgLogo, text='Ebony SyS', width=750, compound=LEFT,
                  padx=5, relief=RAISED, anchor=CENTER, font='Verdana 11 bold italic',
                  bg=dark1, fg=branco, borderwidth=0)
labelLogo.place(x=0, y=0)

# __________________________ POSICIONANDO LOGO NO FRAMETOPO __________________________ ↑
# ---------------------------------- CRIANDO BOTÕES ---------------------------------- ↓

btnNovo = Button(frameEsqueda1, text='Novo', width=10, height=1, bg=dark2,
                 fg=amarelo, font='Verdana 10 bold italic', anchor='center',
                 relief=RIDGE, activebackground=amarelo)
btnNovo.grid(row=0, column=0, sticky=NSEW, pady=10, padx=20)

btnRemover = Button(frameEsqueda1, text='Remover', width=10, height=1, bg=dark2,
                    fg=vermelho, font='Verdana 10 bold italic', anchor='center',
                    relief=RIDGE, activebackground=vermelho)
btnRemover.grid(row=0, column=1, sticky=NSEW, pady=10, padx=20)

btnAtualizar = Button(frameEsqueda1, text='Atualizar', width=10, height=1, bg=dark2,
                      fg=azul, font='Verdana 10 bold italic', anchor='center',
                      relief=RIDGE, activebackground=azul)
btnAtualizar.grid(row=0, column=2, sticky=NSEW, pady=10, padx=20)

# -------------------------------- CRIANDO BOTÕES -------------------------------- ↑
# -------------------------------- CRIANDO LISTBOX ------------------------------- ↓

frameTarefas = Label(frameDireita, text='Tarefas:', width=37, height=1, pady=7,
                     padx=10, relief='flat', font='Courier 20 bold', fg=branco,
                     bg=dark1, anchor=W)
frameTarefas.grid(row=0, column=0, sticky=NSEW, pady=1)

listBox = Listbox(frameDireita, font='Verdana 12', width=1, height=15, bg=dark2,
                  fg=branco, border=10, relief='flat')
listBox.grid(row=1, column=0, sticky=NSEW, padx=10)

# adicionando tarefas para testar
tarefas = [
    'Terminar este App',
    'Começar a versão WEB',
]
for indice, item in enumerate(tarefas):
    listBox.insert(END, f'{indice+1:^2} → {item}')

# -------------------------------- CRIANDO LISTBOX ------------------------------- ↑



janela.mainloop()
