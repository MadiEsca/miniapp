# Conexão com o banco de dados e responsável por criar a tabela caso ela não exista

#import mysql.connector
import sqlite3

#def Conectar():
#    # Criando a conecxão com o banco de dados
#    conexao = mysql.connector.connect(
#        host="localhost",
#        user="root",
#        password="1234",
#        database="escola_mvc" # tabela que iremos utilizar
#    )
#    return conexao

def Conectar():
    # Conectando ao banco de dados
    conexao = sqlite3.connect('escola.db')
    return conexao


def Criar_tabela():
    conexao = Conectar()
    cursor = conexao.cursor()
    query_sql = """CREATE TABLE IF NOT EXISTS TABELA_ALUNOS (
        ID INTEGER PRIMARY KEY,
        Nome VARCHAR(100),
        Email VARCHAR(150),
        Data_nascimento DATE
    )"""
    cursor.execute(query_sql)
    conexao.commit()
    cursor.close()
    conexao.close()