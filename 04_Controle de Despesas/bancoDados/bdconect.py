import sqlite3

com = sqlite3.connect('dados.db')

with com:
    cursor = com.cursor()
    cursor.execute("CREATE TABLE tb_categoria("
                   "id_categoria INTEGER PRIMARY KEY AUTOINCREMENT, "
                   "nome TEXT)")

with com:
    cursor = com.cursor()
    cursor.execute("CREATE TABLE tb_receita("
                   "id_receita INTEGER PRIMARY KEY AUTOINCREMENT, "
                   "categoria TEXT, dt_entrada DATE, "
                   "valor DECIMAL)")

with com:
    cursor = com.cursor()
    cursor.execute("CREATE TABLE tb_gasto("
                   "id_gasto INTEGER PRIMARY KEY AUTOINCREMENT, "
                   "categoria TEXT, "
                   "dt_retirada DATE, "
                   "valor DECIMAL)")


