from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

# Cores _______________↓
dark = "#101010"
preto = "#444466"
branco = "#feffff"
azul = "#6f9fbd"
vermelho = "#ef5350"
numero = "#38576b"
fonte = "#403d3d"

# Cores _______________↑
# Iniciando a janela _________________________________________________________↓

window = Tk()
window.title("Ebony SyS")
window.geometry('550x510')
window.configure(bg=branco)

ttk.Separator(window, orient=HORIZONTAL).grid(row=0, columnspan=1, ipadx=272)

style = ttk.Style(window)
style.theme_use("clam")

# Iniciando a janela _________________________________________________________↑
# Banner _____________________________________________________________________↓

frameBanner = Frame(window, width=550, height=290, relief='flat')
frameBanner.grid(row=1, column=0)
nome = Label(frameBanner, text='Ebony Arts', relief='flat', anchor=CENTER, font=('Fixedsys 20'), fg=preto)
nome.place(x=12, y=15)
categoria = Label(frameBanner, text='Criativo', relief='flat', anchor=CENTER, font=('Ivy 10 bold'), fg=preto)
categoria.place(x=12, y=50)
id = Label(frameBanner, text='#999', relief='flat', anchor=CENTER, font=('Ivy 10 bold'), fg=preto)
id.place(x=12, y=75)

# Imagem
imagem = Image.open('assets/img/pikachu.png')
imagem = imagem.resize((238, 238))
imagem = ImageTk.PhotoImage(imagem)
imagemBanner = Label(frameBanner, relief='flat', image=imagem)
imagemBanner.place(x=60, y=50)

categoria.lift()
id.lift()

# Banner _____________________________________________________________________↑
# Status _____________________________________________________________________↓

status = Label(window, text='Status', relief='flat', anchor=CENTER, font=('Verdana 20'), fg=preto, bg=branco)
status.place(x=15, y=310)
hp = Label(window, text='HP: 100', relief='flat', anchor=CENTER, font=('Verdana 10'), fg=azul, bg=branco)
hp.place(x=15, y=360)
ataque = Label(window, text='Ataque: 200', relief='flat', anchor=CENTER, font=('Verdana 10'), fg=azul, bg=branco)
ataque.place(x=15, y=385)
defesa = Label(window, text='Defesa: 300', relief='flat', anchor=CENTER, font=('Verdana 10'), fg=azul, bg=branco)
defesa.place(x=15, y=410)
velocidade = Label(window, text='Velocidade: 400', relief='flat', anchor=CENTER, font=('Verdana 10'), fg=azul,
                   bg=branco)
velocidade.place(x=15, y=435)
total = Label(window, text='Total: 1000', relief='flat', anchor=CENTER, font=('Verdana 10'), fg=azul, bg=branco)
total.place(x=15, y=460)

# Status _____________________________________________________________________↑
# Habilidades ________________________________________________________________↓

habilidades = Label(window, text='Habilidade', relief='flat', anchor=CENTER, font=('Verdana 20'), fg=preto, bg=branco)
habilidades.place(x=180, y=310)

hab1 = Label(window, text='Pára-raios', relief='flat', anchor=CENTER, font=('Verdana 10'), fg=azul, bg=branco)
hab1.place(x=180, y=360)

hab2 = Label(window, text='Estático', relief='flat', anchor=CENTER, font=('Verdana 10'), fg=azul, bg=branco)
hab2.place(x=180, y=385)

# Habilidades ________________________________________________________________↑
# Botões ________________________________________________________________↓

imgPikachu = Image.open('assets/img/cabeca-pikachu.png')
imgPikachu = imgPikachu.resize((40, 40))
imgPikachu = ImageTk.PhotoImage(imgPikachu)
imagemBanner = Button(window, image=imgPikachu, text='Pikachu', font=('Verdana 12'), width=150, relief='raised',
                      overrelief=RIDGE, compound=RIGHT, anchor=CENTER, padx=5, fg=preto, bg=branco)
imagemBanner.place(x=375, y=10)

imgBulbasaur = Image.open('assets/img/cabeca-bulbasaur.png')
imgBulbasaur = imgBulbasaur.resize((40, 40))
imgBulbasaur = ImageTk.PhotoImage(imgBulbasaur)
imagemBanner = Button(window, image=imgBulbasaur, text='Bulbasaur', font=('Verdana 12'), width=150, relief='raised',
                      overrelief=RIDGE, compound=RIGHT, anchor=CENTER, padx=5, fg=preto, bg=branco)
imagemBanner.place(x=375, y=65)

imgCharmander = Image.open('assets/img/cabeca-charmander.png')
imgCharmander = imgCharmander.resize((40, 40))
imgCharmander = ImageTk.PhotoImage(imgCharmander)
imagemBanner = Button(window, image=imgCharmander, text='Charmander', font=('Verdana 12'), width=150, relief='raised',
                      overrelief=RIDGE, compound=RIGHT, anchor=CENTER, padx=5, fg=preto, bg=branco)
imagemBanner.place(x=375, y=120)

imgDragonite = Image.open('assets/img/cabeca-dragonite.png')
imgDragonite = imgDragonite.resize((40, 40))
imgDragonite = ImageTk.PhotoImage(imgDragonite)
imagemBanner = Button(window, image=imgDragonite, text='Dragonite', font=('Verdana 12'), width=150, relief='raised',
                      overrelief=RIDGE, compound=RIGHT, anchor=CENTER, padx=5, fg=preto, bg=branco)
imagemBanner.place(x=375, y=175)

imgGengar = Image.open('assets/img/cabeca-gengar.png')
imgGengar = imgGengar.resize((40, 40))
imgGengar = ImageTk.PhotoImage(imgGengar)
imagemBanner = Button(window, image=imgGengar, text='Gengar', font=('Verdana 12'), width=150, relief='raised',
                      overrelief=RIDGE, compound=RIGHT, anchor=CENTER, padx=5, fg=preto, bg=branco)
imagemBanner.place(x=375, y=230)

imgGyarados = Image.open('assets/img/cabeca-gyarados.png')
imgGyarados = imgGyarados.resize((40, 40))
imgGyarados = ImageTk.PhotoImage(imgGyarados)
imagemBanner = Button(window, image=imgGyarados, text='Gyarados', font=('Verdana 12'), width=150, relief='raised',
                      overrelief=RIDGE, compound=RIGHT, anchor=CENTER, padx=5, fg=preto, bg=branco)
imagemBanner.place(x=375, y=285)

# Botões ________________________________________________________________↑
# onclick ________________________________________________________________↓


# onclick ________________________________________________________________↑


window.mainloop()

'''
Desenvolvido por Leonardo Alves
Contato: leon4rdoalvess@gmail.com
'''
