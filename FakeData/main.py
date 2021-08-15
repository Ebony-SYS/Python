import PySimpleGUI as sg
import os
from faker import Faker

sg.theme('Darkblue')

layout = [
    [sg.Text('Vamos lá, defina quais e quantos dados serão gerados?')],
    [sg.Button('Nome', size=(20, 0)), sg.Input(key='name', size=(30, 0))],
    [sg.Button('Telefone', size=(20, 0)), sg.Input(key='phone', size=(30, 0))],
    [sg.Button('Email', size=(20, 0)), sg.Input(key='email', size=(30, 0))],
    [sg.Button('Endereço', size=(20, 0)), sg.Input(key='address', size=(30, 0))],
    [sg.Button('Cidade', size=(20, 0)), sg.Input(key='city', size=(30, 0))],
    [sg.Button('Estado', size=(20, 0)), sg.Input(key='state', size=(30, 0))],
    [sg.Button('País', size=(20, 0)), sg.Input(key='country', size=(30, 0))],
    [sg.Button('CEP', size=(20, 0)), sg.Input(key='zipCode', size=(30, 0))],
    [sg.Button('CPF', size=(20, 0)), sg.Input(key='cpf', size=(30, 0))],
    [sg.Button('RG', size=(20, 0)), sg.Input(key='rg', size=(30, 0))],
    [sg.Button('CNPJ', size=(20, 0)), sg.Input(key='cnpj', size=(30, 0))],
    [sg.Text(size=(40, 1), key='-OUTPUT-')],
    [sg.Button('Gerar Dados'), sg.Button('Salvar Dados'), sg.Button('Finalizar'),
     sg.Button('@ebony.programador')]
]

window = sg.Window('Dados Aleatórios | @ebony.programador', layout=layout)

fake = Faker('pt-BR')
Faker.seed(0)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Finalizar':
        break

