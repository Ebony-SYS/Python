import PySimpleGUI as sg
import os
from inspect import Traceback
from functionalities.functionalities import initWindow, Speaking

windowOne = initWindow()

while True:
    window, event, values = sg.read_all_windows()
    if window == windowOne and event == 'Exit' or event == sg.WIN_CLOSED:
        break
    if window == windowOne and event == 'fileReading':
        filePath = values['-FILE-']
        fileName = os.path.basename(filePath)
        window['fileSelected'].update(f'lido → {fileName}', text_color='green')
        try:
            if fileName[-4:] == '.txt':
                with open(filePath) as text_to_read:
                    txt = text_to_read.read()
                    Speaking(txt)
            else:
                window['fileSelected'].update('Ops, ainda não suporto este arquivo!', text_color='red')
        except:
            window['fileSelected'].update('Ops, este arquivo está vazio!', text_color='red')
        if filePath == '':
            window['fileSelected'].update('Hey, selecione um arquivo!', text_color='red')
window.close()

'''
Desenvolvido por Leonardo Alves
Contato: leon4rdoalvess@gmail.com
'''
