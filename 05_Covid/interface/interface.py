from tkinter import *
from tkinter import ttk
from PIL import Image
import requests
import string
import json
import datetime

preto = '#000'
branco = '#fff'
vermelho = '#cc1d4e'
amarelo = '#d1d420'
verde = '#59b356'
cinza = '#d9d9d9'
dark = '#101010'
dark1 = '#1e1e1e'

# ----------------------------- API -----------------------------↓
# API → https://covid19.mathdro.id/api

response = requests.get('https://covid19.mathdro.id/api')
info = response
info = json.loads(info.text)

infectados = info['confirmed']['value']
recuperados = info['recovered']['value']
perdidos = info['deaths']['value']
update = info['lastUpdate']
update = datetime.datetime.strptime(update, '%Y-%m-%dT%H:%M:%S.000Z')
# update = update.strftime('%a | %d.%m.%Y | %H:%M')
update = update.strftime('%d.%B.%Y | %Hh%Mmin')

# ------------------------------ JANELA PRINCIPAL -------------------------------↓
janela = Tk()
janela.resizable(width=False, height=False)
janela.geometry('835x360')
janela.title('Ebony SYS - Leonardo Alves')
janela.configure(bg=dark)
# ------------------------------ JANELA PRINCIPAL -------------------------------↑

# ----------------------------------- FRAME'S -----------------------------------↓
frameBanner = Frame(janela, width=835, height=50, bg=dark, relief='flat')
frameBanner.grid(row=0, column=0, columnspan=3, sticky=N)

frameInfectados = Frame(janela, width=220, height=120, bg=dark1, relief='flat')
frameInfectados.grid(row=1, column=0, sticky=NW, pady=5, padx=5)

frameRecuperados = Frame(janela, width=220, height=120, bg=dark1, relief='flat')
frameRecuperados.grid(row=1, column=1, sticky=NW, padx=5, pady=5)

framePerdidos = Frame(janela, width=220, height=120, bg=dark1, relief='flat')
framePerdidos.grid(row=1, column=2, sticky=NW, pady=5, padx=5)

frameSelect = Frame(janela, width=835, height=50, bg=dark, relief='flat')
frameSelect.grid(row=2, column=0, columnspan=3, sticky=N, pady=10)
# ----------------------------------- FRAME'S -----------------------------------↑

# ----------------------------------- BANNER ------------------------------------↓
img = Image.open('imgCovid.png')
img = img.resize((50, 50))
img.save('Covid.png')
imagem = PhotoImage(file='Covid.png')

imageBanner = Label(frameBanner, image=imagem, width=350, pady=20, relief='flat',
                    bg=dark, anchor=NE)
imageBanner.grid(row=0, column=0, pady=5)

labelBanner = Label(frameBanner, text='COVID-19', width=20, height=1, pady=20,
                    relief='flat', anchor=NW, font='Helvetica 25 bold',
                    bg=dark, fg=cinza)
labelBanner.grid(row=0, column=1, pady=5)

# ----------------------------------- BANNER -----------------------------------↑

# ----------------------------------- INFECTADOS -------------------------------↓
labelInfectados = Label(frameInfectados, text='INFECTADOS', width=20, height=1,
                        pady=7, padx=0, relief='flat', anchor=NW, bg=dark1,
                        font='Courier 15 bold', fg=cinza)
labelInfectados.grid(row=0, column=0, padx=13, pady=1)

mostrarInfectados = Label(frameInfectados, text=infectados, width=12, height=1,
                          pady=7, padx=0, relief='flat', anchor=NW, bg=dark1,
                          font='Courier 25 bold', fg=cinza)
mostrarInfectados.grid(row=1, column=0, pady=1)

infoInfectados = Label(frameInfectados, text='Última atualização ↓', width=27,
                       height=1, pady=7, padx=0, relief='flat', anchor=NW,
                       bg=dark1, font='Courier 11 bold', fg=cinza)
infoInfectados.grid(row=2, column=0, pady=0, padx=13)

mostrarDtInfectados = Label(frameInfectados, text=str(update),
                          width=27, height=1, pady=7, padx=0, relief='flat',
                          anchor=NW, bg=dark1, font='Courier 11 bold', fg=cinza)
mostrarDtInfectados.grid(row=3, column=0, pady=0, padx=13)

linhaInfectados = Label(frameInfectados, text='', width=19, height=1,
                        pady=1, padx=0, relief='flat', anchor=NW, bg=amarelo,
                        font='Courier 1 bold')
linhaInfectados.grid(row=4, column=0, padx=0, pady=0, sticky=NSEW)
# ----------------------------------- INFECTADOS -------------------------------↑

# ----------------------------------- RECUPERADOS ------------------------------↓
labelRecuperados = Label(frameRecuperados, text='RECUPERADOS', width=20, height=1,
                         pady=7, padx=0, relief='flat', anchor=NW, bg=dark1,
                         font='Courier 15 bold', fg=cinza)
labelRecuperados.grid(row=0, column=0, padx=13, pady=1)

mostrarRecuperados = Label(frameRecuperados, text=infectados - perdidos, width=12, height=1,
                           pady=7, padx=0, relief='flat', anchor=NW, bg=dark1,
                           font='Courier 25 bold', fg=cinza)
mostrarRecuperados.grid(row=1, column=0, pady=1)

infoRecuperados = Label(frameRecuperados, text='Última atualização ↓', width=27,
                        height=1, pady=7, padx=0, relief='flat', anchor=NW,
                        bg=dark1, font='Courier 11 bold', fg=cinza)
infoRecuperados.grid(row=2, column=0, pady=0, padx=13)

mostrarDtRecuperados = Label(frameRecuperados, text=str(update),
                           width=27, height=1, pady=7, padx=0, relief='flat',
                           anchor=NW, bg=dark1, font='Courier 11 bold', fg=cinza)
mostrarDtRecuperados.grid(row=3, column=0, pady=0, padx=13)

linhaRecuperados = Label(frameRecuperados, text='', width=19, height=1,
                         pady=1, padx=0, relief='flat', anchor=NW, bg=verde,
                         font='Courier 1 bold')
linhaRecuperados.grid(row=4, column=0, padx=0, pady=0, sticky=NSEW)
# ----------------------------------- RECUPERADOS ------------------------------↑

# ------------------------------------ PERDIDOS --------------------------------↓
labelPerdidos = Label(framePerdidos, text='PERDIDOS', width=20, height=1,
                      pady=7, padx=0, relief='flat', anchor=NW, bg=dark1,
                      font='Courier 15 bold', fg=cinza)
labelPerdidos.grid(row=0, column=0, padx=13, pady=1)

mostrarPerdidos = Label(framePerdidos, text=perdidos, width=12, height=1,
                        pady=7, padx=0, relief='flat', anchor=NW, bg=dark1,
                        font='Courier 25 bold', fg=cinza)
mostrarPerdidos.grid(row=1, column=0, pady=1)

infoPerdidos = Label(framePerdidos, text='Última atualização ↓', width=27,
                     height=1, pady=7, padx=0, relief='flat', anchor=NW,
                     bg=dark1, font='Courier 11 bold', fg=cinza)
infoPerdidos.grid(row=2, column=0, pady=0, padx=13)

mostrarDtPerdidos = Label(framePerdidos, text=str(update),
                        width=27, height=1, pady=7, padx=0, relief='flat',
                        anchor=NW, bg=dark1, font='Courier 11 bold', fg=cinza)
mostrarDtPerdidos.grid(row=3, column=0, pady=0, padx=13)

linhaPerdidos = Label(framePerdidos, text='', width=19, height=1, pady=1, padx=0,
                      relief='flat', anchor=NW, bg=vermelho, font='Courier 1 bold')
linhaPerdidos.grid(row=4, column=0, padx=0, pady=0, sticky=NSEW)
# ------------------------------------ PERDIDOS --------------------------------↑

# ------------------------------------- PAÍSES ---------------------------------↓
paises = ['Brazil', 'USA', 'Portugal', 'France', 'Spain', 'Angola', 'Global']

labelPais = Label(frameSelect, text='Selecione um país:', width=15, height=1,
                  pady=7, padx=0, relief='flat', anchor=NW, font='Ivy 11 bold',
                  bg=dark, fg=cinza)
labelPais.grid(row=0, column=0, pady=1, padx=13)

boxPais = ttk.Combobox(frameSelect, width=11, font='Ivy 10 bold')
boxPais['values'] = paises
boxPais.grid(row=0, column=1, padx=0, pady=13)


# ----------------------------- API -----------------------------↓
# API(países) → https://covid19.mathdro.id/api/countries/Brazil

def selecionando(eventObject):

    if boxPais.get() == 'Global':
        response = requests.get('https://covid19.mathdro.id/api')
        info = response
        info = json.loads(info.text)

        infectados = info['confirmed']['value']
        recuperados = info['recovered']['value']
        perdidos = info['deaths']['value']

        mostrarInfectados.configure(text=infectados)
        mostrarRecuperados.configure(text=infectados - perdidos)
        mostrarPerdidos.configure(text=perdidos)

    else:
        selectPais = boxPais.get()
        response = requests.get(f'https://covid19.mathdro.id/api/countries/{selectPais}')
        info = response
        info = json.loads(info.text)

        infectados = info['confirmed']['value']
        recuperados = info['recovered']['value']
        perdidos = info['deaths']['value']
        update = info['lastUpdate']
        update = datetime.datetime.strptime(update, '%Y-%m-%dT%H:%M:%S.000Z')
        # update = update.strftime('%a | %d.%m.%Y | %H:%M')
        update = update.strftime('%d.%B.%Y | %Hh%Mmin')

        mostrarInfectados.configure(text=infectados)
        mostrarRecuperados.configure(text=infectados - perdidos)
        mostrarPerdidos.configure(text=perdidos)

        print(infectados, recuperados, perdidos, update)


boxPais.bind('<<ComboboxSelected>>', selecionando)
# ----------------------------- API -----------------------------↑


janela.mainloop()

'''
Desenvolvido por Leonardo Alves
Contato: leon4rdoalvess@gmail.com
'''