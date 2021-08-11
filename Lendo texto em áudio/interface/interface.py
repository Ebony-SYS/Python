import PySimpleGUI as sg
import os
from functionalities.functionalities import initWindow, speaking, getAudio, windowSpeechRecognition
from inspect import Traceback

windowOne, windowTwo = initWindow(), None

while True:
    event, value, window = sg.read_all_windows()

    if window == windowOne and event == 'Exit' or event == sg.WIN_CLOSED:
        break

    if window == windowOne and event == 'fileReading':
        filePath = value['-FILE-']
        fileName = os.path.basename(filePath)
        window['fileSelected'].update(f'Arquivo: {fileName}', text_color='green')

        try:
            if fileName[-4:] == '.txt':
                with open(filePath) as textToRead:
                    txt = textToRead.read()
                    speaking(txt)

            else:
                window['fileSelected'].update('Ops, arquivo não suportado.', text_color='red')
        except:
            window['fileSelected'].update('Arquivo está vazio.', text_color='red')

        if filePath == '':
            window['fileSelected'].update('Um arquivo precisa ser selecionado.', text_color='red')

    if window == windowOne and event == 'speakText':
        windowTwo = windowSpeechRecognition()
        windowOne.hide()

    if window == windowTwo and event == 'back':
        windowTwo.hide()
        windowOne.un_hide()

    try:
        if window == windowTwo and event == 'txtButton':
            window['informationText'].update('Arquivo criado com sucesso', text_color='green')
            with open('file.txt', 'w', encoding='utf8') as fileText:
                said = getAudio()
                fileText.write(said)

    except:
        window['informationText'].update('Ops, algo deu errado.', text_color='red')

window.close()





