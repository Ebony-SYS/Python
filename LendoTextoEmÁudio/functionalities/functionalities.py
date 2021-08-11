import PySimpleGUI as sg
import os
import speech_recognition as sr
from gtts import gTTS
from playsound import playsound


def initWindow():
    fileTypes = [('Todos os arquivos', '*.*')]
    layout = [[sg.Text('Selecione um arquivo para começar')],
              [sg.Text(size=(23, 1), key='fileSelected')],
              [sg.Button('speakText', key='speakText'),
               sg.Input(size=(25, 1), key='-FILE-'),
               sg.FileBrowse(fileTypes=fileTypes, key='fileBrowse'),
               sg.Button('fileReading', key='fileReading')]]

    return sg.Window('text reading', layout=layout, finalize=True, element_justification='c')


def windowSpeechRecognition():
    ...


def getAudio():
    ...


def speaking():
    ...
