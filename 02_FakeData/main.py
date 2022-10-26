import PySimpleGUI as sg
import os
from faker import Faker

sg.theme('Darkblue')

layout = [
    [sg.Text('Vamos lá, defina quais e quantos dados serão gerados?')],
    [sg.Button('Nome', size=(20, 0)), sg.Input(key='name', size=(50, 0))],
    [sg.Button('Telefone', size=(20, 0)), sg.Input(key='phone', size=(50, 0))],
    [sg.Button('Email', size=(20, 0)), sg.Input(key='email', size=(50, 0))],
    [sg.Button('Endereço', size=(20, 0)), sg.Input(key='address', size=(50, 0))],
    [sg.Button('Cidade', size=(20, 0)), sg.Input(key='city', size=(50, 0))],
    [sg.Button('Estado', size=(20, 0)), sg.Input(key='state', size=(50, 0))],
    [sg.Button('País', size=(20, 0)), sg.Input(key='country', size=(50, 0))],
    [sg.Button('CEP', size=(20, 0)), sg.Input(key='zipCode', size=(50, 0))],
    [sg.Button('Profissão', size=(20, 0)), sg.Input(key='job', size=(50, 0))],
    [sg.Button('Data de Nascimento', size=(20, 0)), sg.Input(key='dtBirth', size=(50, 0))],
    [sg.Button('CNPJ', size=(20, 0)), sg.Input(key='cnpj', size=(50, 0))],
    [sg.Button('CPF', size=(20,0)), sg.Input(key='cpf',size=(50,0))],
    [sg.Button('RG', size=(20,0)), sg.Input(key='rg', size=(50,0))],
    [sg.Text(size=(60, 1), key='-OUTPUT-')],
    [sg.Button('Gerar todos os dados', size=(16)), sg.Button('Salvar Dados', size=(12)), 
     sg.Button('Finalizar', size=(12)), sg.Button('@ebony.programador', button_color='lightgreen', size=(19))]
]

window = sg.Window('Dados Aleatórios | EBONY SYS', layout=layout)

fake = Faker('pt-BR')
Faker.seed(0)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Finalizar':
        break       

    elif event == "Nome":
        nameRandom = fake.unique.name()
        window['name'].update(nameRandom)
        
    elif event == "Telefone":
        phoneRandom = fake.phone_number()
        window['phone'].update(phoneRandom)

    elif event == "Email":
        emailRandom = fake.ascii_free_email()
        window['email'].update(emailRandom)
        
    elif event == "Endereço":
        addressRandom = fake.address()
        window['address'].update(addressRandom)
    
    elif event == "Cidade":
        cityRandom = fake.city()
        window['city'].update(cityRandom)
        
    elif event == "Estado":
        stateRandom = fake.state()
        window['state'].update(stateRandom)
        
    elif event == "País":
        countryRandom = fake.current_country()
        window['country'].update(countryRandom)
        
    elif event == "CEP":
        zipCodeRandom = fake.ean(length=8)
        window['zipCode'].update(zipCodeRandom)
    
    elif event == "Profissão":
        jobRandom = fake.job()
        window['job'].update(jobRandom)
        
    elif event == "Data de Nascimento":
        dtNascRandom = fake.date_of_birth()
        window['dtBirth'].update(dtNascRandom)
        
    elif event == "CNPJ":
        cnpjRandom = fake.cnpj()
        window['cnpj'].update(cnpjRandom)
    
    elif event == "CPF":
        cpfRandom = fake.cpf()
        window['cpf'].update(cpfRandom)

    elif event == "RG":
        rgRandom = fake.rg()
        window['rg'].update(rgRandom)

    elif event == "Gerar todos os dados":
        nameRandom = fake.name()
        phoneRandom = fake.phone_number()
        emailRandom = fake.email()
        addressRandom = fake.address()
        cityRandom = fake.city()
        stateRandom = fake.state()
        countryRandom = fake.current_country()
        zipCodeRandom = fake.ean(length=8)
        jobRandom = fake.job()
        dtNascRandom = fake.date_of_birth()
        cnpjRandom = fake.cnpj()
        cpfRandom = fake.cpf()
        rgRandom = fake.rg()
        window['name'].update(nameRandom)
        window['phone'].update(phoneRandom)
        window['email'].update(emailRandom)
        window['address'].update(addressRandom)
        window['city'].update(cityRandom)
        window['state'].update(stateRandom)
        window['country'].update(countryRandom)
        window['zipCode'].update(zipCodeRandom)
        window['job'].update(jobRandom)
        window['dtBirth'].update(dtNascRandom)
        window['cnpj'].update(cnpjRandom)
        window['cpf'].update(cpfRandom)
        window['rg'].update(rgRandom)
        
    try:
        if event == "Salvar Dados":
            with open ('dadosFalsos.txt', 'a', encoding='utf-8', newline='') as arquivo:
                arquivo.write(f"Nome:  {nameRandom}{os.linesep}Telefone: {phoneRandom}{os.linesep}"
                              f"Email: {emailRandom}{os.linesep}Endereço: {addressRandom}{os.linesep}"
                              f"Cidade: {cityRandom}{os.linesep}Estado: {stateRandom}{os.linesep}"
                              f"País: {countryRandom}{os.linesep}CEP: {zipCodeRandom}{os.linesep}"
                              f"Profissão: {jobRandom}{os.linesep}Dt. Nascimento: {dtNascRandom}{os.linesep}"
                              f"CNPJ: {cnpjRandom}{os.linesep}CPF: {cpfRandom}{os.linesep}"
                              f"RG: {rgRandom}{os.linesep}")
                              
            window["-OUTPUT-"].update('Dados salvos com sucesso!')
                
    except NameError as erro:
        print('\nAlgo errado não está certo!\n')
        
'''
Desenvolvido por Leonardo Alves
Contato: leon4rdoalvess@gmail.com
'''
