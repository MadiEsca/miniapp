from flask_wtf import FlaskForm
from wtforms import fields
from wtforms.validators import DataRequired, Email


class AlunoForm(FlaskForm):
    _DataRequiredMessage = str("Esse campo não pode estar vazio")
    _EmailMessage = str("Digite um email válido")

    aluno_nome = fields.StringField(label="Nome", name="nome", validators=[DataRequired(message=_DataRequiredMessage)]) #tipo_campo("nome do campo")
    aluno_data_nascimento = fields.DateField(label="Data de nascimento", name="data_nascimento", validators=[DataRequired(message=_DataRequiredMessage)]) #tipo_campo("nome do campo")
    aluno_email = fields.EmailField(label="Email", name="email", validators=[Email(message=_EmailMessage)]) #tipo_campo("nome do campo")
    enviar = fields.SubmitField(label="Enviar", name="enviar") #tipo_campo("nome do campo")