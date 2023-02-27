from tkinter import filedialog as fd
import os
import shutil

# root cores
preto = '#000'
branco = '#fff'
dark1 = '#3F3F3F'
dark2 = '#1f1f1f'

amarelo = '#ffff00'
azul_claro = '#836fff'
azul_escuro = '#000080'
verde_claro = '#00ff00'
verde_escuro = '#228d22'
vermelho = '#ff0000'
violeta = '#9400f3'
rosa = '#ff00ff'
laranja = '#ff8c00'

cores = [
    amarelo, azul_claro, azul_escuro,
    verde_claro, verde_escuro, vermelho,
    violeta, rosa, laranja
]

# root fonte
fonte_principal = 'Ubuntu 16 bold'
cor_fonte_principal = '#f0f8ff'
fonte_secundaria = 'Ubuntu 14'
cor_fonte_secundaria = '#ffd700'

# root imagens
img_logo = '../assets/img/logo.png'
icone_pasta = '../assets/img/pasta.png'

global pasta


# função para contar pastas
def contarPastasArquivos(caminho, extencao):
    qtd_pastas = 0
    qtd_arquivos = 0

    for item in os.listdir(caminho):
        if os.path.isfile(os.path.join(caminho, item)) and item.endswith(extencao):
            qtd_arquivos += 1
        elif os.path.isdir(os.path.join(caminho, item)):
            qtd_pastas += 1
            subpasta_path = os.path.join(caminho, item)
            qtd_subarquivos, qtd_subpastas = contarPastasArquivos(subpasta_path, extencao)
            qtd_pastas += qtd_subpastas
            qtd_arquivos += qtd_subarquivos

    return qtd_pastas, qtd_arquivos


# função para escolher uma pasta
def escolherPasta():
    global pasta
    pasta = fd.askdirectory()

    extencoes = ['.txt', '.csv', '.xlsx', '.pdf', '.json', '.jpg', '.jpeg', '.png', '.mpeg',
                 '.mp3', '.mp4', '.avi', '.html', '.css', '.sass', '.js', '.py', '.sql', '.ty']

    extencoes_combobox = []
    extencoes_encontradas = []
    extencoes_quantidade = []
    quantidade_pastas = 0

    for item in extencoes:
        caminho = pasta
        extencao = item
        qtd_arquivos, qtd_pastas = contarPastasArquivos(caminho, extencao)

        if qtd_arquivos <= 0:
            pass
        else:
            extencoes_encontradas.append(f'{item}: {str(qtd_arquivos)}')