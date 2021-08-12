import PySimpleGUI as sg
import os
import speech_recognition as sr
from gtts import gTTS
from playsound import playsound


def initWindow():
    sg.theme('Dark')
    fileTypes = [('Todos os arquivos', '*.*')]
    layout = [[sg.Text('Escolha um arquivo para iniciar!!!')],
              [sg.Text(size=(23, 1), key='fileSelected')],
              [  # sg.Button('Ouvir', key='speakText'),
                  sg.Input(size=(25, 1), key='-FILE-'),
                  sg.FileBrowse(file_types=fileTypes, key='fileBrowse'),
                  sg.Button('Ler texto', key='fileReading')]]

    return sg.Window('text reading', layout=layout, finalize=True, element_justification='c')


def windowSpeechRecognition():
    ...


def getAudio():
    rd = sr.Recognizer()
    with sr.Microphone() as source:
        audio = rd.listen(source)
        said = ''
        said = rd.recognize_google(audio, language='pt-BR')
    return said


def speaking():
    ...
