import tkinter


def Tela_inicial():
    root_tela_inicial = tkinter.Tk()
    root_tela_inicial.geometry("920x700+0+0")
    root_tela_inicial.resizable(width=False, height=False)
    root_tela_inicial.title('Ebony Sys || JOGOS')

    image = tkinter.PhotoImage(file='img/back.png')
    image = image.subsample(1, 1)
    labelimage = tkinter.Label(image=image)
    labelimage.place(x=0, y=0, relwidth=1.0, relheight=1.0)

    snake = tkinter.Button(root_tela_inicial, text="Snake", bg='light blue', font='Ubuntu 18 italic', bd=2,
                           relief='raised', activebackground='green', width=35)
    snake.place(x=210, y=250)

    corrida = tkinter.Button(root_tela_inicial, text='Corrida', bg='light blue', font='Ubuntu 18 italic', bd=2,
                             relief='raised', activebackground='blue', width=35)
    corrida.place(x=210, y=300)

    sinuca = tkinter.Button(root_tela_inicial, text='Sinuca', bg='light blue', font='Ubuntu 18 italic', bd=2,
                            relief='raised', activebackground='yellow', width=35)
    sinuca.place(x=210, y=350)

    sair = tkinter.Button(root_tela_inicial, text="Sair", bg='light blue', font='Ubuntu 18 italic', bd=2,
                          relief='raised', activebackground='red', width=35, command="destroy .")
    sair.place(x=210, y=400)

    root_tela_inicial.mainloop()


Tela_inicial()
