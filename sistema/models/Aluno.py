# Criação do model do aluno
# Arquivo responsável por cuidas das regras de negócio relacionadas a entidade aluno dentro do banco de dados

from datetime import datetime
from database import Conectar
from repositories.Aluno_Repository import salvar


class Aluno:
    def __init__(self, nome, data, email):
        self.nome = nome
        self.data = datetime.strptime(data, "%Y/%m/%d").date() # String parsed for time (String parseada/transformada em data)
        self.email = email

        self.matricula = '' # Será gerada

    def gerar_numero_matricula(self):
        # Será utilizado para gerar a matricula do aluno
        nome_aluno = self.nome
        nascimento_aluno = self.data

        matricula_gerada = f"{nome_aluno[0:3]}{nascimento_aluno[3]}" 

        return f"Responsável por gerar a matricula individual de cada aluno: {matricula_gerada}" #tres 1° caracteres do nome + ano nascimento