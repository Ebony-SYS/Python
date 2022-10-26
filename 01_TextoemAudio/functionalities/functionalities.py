import PySimpleGUI as sg
import os
from gtts import gTTS, lang
from playsound import playsound


def Speaking(text):
    textSpeaking = gTTS(text=text, lang='pt-br', slow=False)
    filename = 'audio.mp3'
    textSpeaking.save(filename)
    playsound(filename)
    os.remove(filename)


def initWindow():
    sg.theme('Dark')
    fileTypes = [("Todos arquivos", "*.*")]
    layout = [[sg.Text('Vamos lá, escolha um arquivo!')],
              [sg.Text(size=(30, 1), key='fileSelected')],
              [sg.Input(size=(30, 1), key="-FILE-"),
               sg.FileBrowse(file_types=fileTypes, key='file_browse'),
               sg.Button('Ler arquivo', key='fileReading')]]

    return sg.Window('@ebony.programador | Códigos Simples', layout=layout, finalize=True, element_justification='c')

'''
Desenvolvido por Leonardo Alves
Contato: leon4rdoalvess@gmail.com
'''