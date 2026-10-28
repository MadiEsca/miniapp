# Repository responsável por cuidar das operações que tem a ver com o banco de dados referente a entidade alunos
#from models.Aluno import Aluno
from database import Conectar

# ===== LISTAGEM =====

# Lista todos os usuários cadastrados dentro do banco
def listar():
    conexao = Conectar()
    cursor = conexao.cursor()
    query_sql = """SELECT * FROM TABELA_ALUNOS"""
    cursor.execute(query_sql)
    resposta = cursor.fetchall()
    cursor.close()
    conexao.close()
    return resposta

# Lista o usuário que contém o email correspondente
def listar_email(email:str):
    conexao = Conectar()
    cursor = conexao.cursor()
    query_sql = "SELECT * FROM TABELA_ALUNOS WHERE Email = :email", (email,)
    cursor.execute(query_sql)
    resposta = cursor.fetchall()
    cursor.close()
    conexao.close()
    return resposta

# ===== CRIAÇÃO=====

# Função utilizada em conjunto com o model para criar um registro do aluno no banco de dados
def salvar(nome_aluno, data_nascimento_aluno, email_aluno):
    conexao = Conectar()
    cursor = conexao.cursor()
    query_sql = """INSERT INTO TABELA_ALUNOS (Nome, Email, Data_nascimento) VALUES (:Nome, :Email, :Data_nascimento)"""
    #valores = (nome_incricao, data_inscricao, email_inscricao) # Valores tirados do próprio objeto quando criado
    cursor.execute(query_sql, {
        "Nome":nome_aluno,
        "Email": email_aluno,
        "Data_nascimento":data_nascimento_aluno,
        })
    conexao.commit()
    cursor.close()
    conexao.close()