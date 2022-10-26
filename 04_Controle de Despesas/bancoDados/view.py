import sqlite3 as sql

com = sql.connect('dados.db')


def inserirCategoria(c):
    with com:
        cursor = com.cursor()
        query = 'INSERT INTO tb_categoria (nome) VALUES (?)'
        cursor.execute(query, c)  # necessário inserir uma lista e não uma string


def deletarCategoria(c):
    with com:
        cursor = com.cursor()
        query = "DELETE FROM tb_categoria WHERE id_categoria=?"
        cursor.execute(query, c)


def verCategoria():
    categorias = []
    with com:
        cursor = com.cursor()
        cursor.execute("SELECT * FROM tb_categoria")
        linhas = cursor.fetchall()
        for linha in linhas:
            categorias.append(linha)
    return categorias


def inserirReceita(r):
    with com:
        cursor = com.cursor()
        query = 'INSERT INTO tb_receita (categoria, dt_entrada, valor) VALUES (?,?,?)'
        cursor.execute(query, r)  # necessário inserir uma lista e não uma string


def deletarReceita(r):
    with com:
        cursor = com.cursor()
        query = "DELETE FROM tb_receita WHERE id_receita=?"
        cursor.execute(query, r)


def verReceita():
    receitas = []
    with com:
        cursor = com.cursor()
        cursor.execute("SELECT * FROM tb_receita")
        linhas = cursor.fetchall()
        for linha in linhas:
            receitas.append(linha)
    return receitas


def inserirGasto(g):
    with com:
        cursor = com.cursor()
        query = 'INSERT INTO tb_gasto (categoria, dt_retirada, valor) VALUES (?,?,?)'
        cursor.execute(query, g)  # necessário inserir uma lista e não uma string


def deletarGasto(g):
    with com:
        cursor = com.cursor()
        query = "DELETE FROM tb_gasto WHERE id_gasto=?"
        cursor.execute(query, g)


def verGasto():
    gastos = []
    with com:
        cursor = com.cursor()
        cursor.execute("SELECT * FROM tb_gasto")
        linhas = cursor.fetchall()
        for linha in linhas:
            gastos.append(linha)
    return gastos

'''
Desenvolvido por Leonardo Alves
Contato: leon4rdoalvess@gmail.com
'''