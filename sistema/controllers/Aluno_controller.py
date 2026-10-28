# Criação do controller do usuário
# Responsável pela interação entre repositorys e o usuário
from flask import request, render_template, redirect
from repositories.Aluno_Repository import salvar
from models.Aluno import Aluno
from views.Aluno_form import AlunoForm

# ===== ROTAS =====

# INICIO
def index():
    return render_template("index.html")

# CADASTRAMENTO
def formulario():
    form = AlunoForm() # Cria o formulário

    if form.validate_on_submit(): # Valida se as informações estão todas corretas
        cadastrar() # Realiza o cadastro do usuário
        return redirect("/")
    # Carrega o formulário, criado em python, para o html
    return render_template("formulario.html", form=form) # isso deve ser feito com base no usuário autenticado (implementar autenticação)

# ===== AÇÔES =====

def cadastrar():
    nome = request.form["nome"] # Acessando os dados do campo "nome"
    data_nascimento = request.form["data_nascimento"].replace("-", "/") # Acessando os dados do campo "data_nascimento" e substituindo "-" por "/"
    email = request.form["email"] # Acessando os dados do campo "email"
    
    novo_aluno = Aluno(nome, data_nascimento, email) # Criando o objeto do aluno
    print("USUÁRIO SALVO COM SUCESSO")
    return salvar(novo_aluno.nome, novo_aluno.data, novo_aluno.email)