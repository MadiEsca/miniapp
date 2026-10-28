# módulo principal que irá rodar a aplicação

from flask import Flask, request
from controllers.Aluno_controller import index, formulario
from controllers.Aluno_controller import cadastrar
from database import Criar_tabela

app = Flask(__name__)
app.config['SECRET_KEY'] = "rklamrmeu" # Utilizado para habilitar o CORS


@app.route("/", methods={"GET"})
def pagina_inicial():
    return index()

@app.route("/cadastro", methods=['GET', 'POST']) # Rota que carrega o formulário
def pagina_cadastro():
    return formulario() # Requisição é do tipo POST

if __name__ == "__main__":
    app.run(debug=True)
    Criar_tabela()