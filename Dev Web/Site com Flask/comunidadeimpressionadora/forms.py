#AQUI É ONDE CRIA TODOS OS FORMULÁRIOS QUE IRÁ UTILIZAR
# Importando os formulários, tipos de campos e validações de campos.

from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from comunidadeimpressionadora.models import Usuario
from flask_login import current_user

class FormCriarConta(FlaskForm):
    username = StringField ('Nome de Usuário', validators=[DataRequired()])
    email = StringField ('E-mail', validators=[DataRequired(), Email()])
    senha = PasswordField ('Senha', validators=[DataRequired(), Length(6,20)])
    confirmacao = PasswordField ('Confirmar Senha', validators=[DataRequired(), EqualTo('senha')])
    botao_criar = SubmitField ('Criar Conta')

    #Validar se o email já existe no banco de dados
    def validate_email(self, email):
        usuario = Usuario.query.filter_by(email=email.data).first()
        if usuario:
            raise ValidationError('E-mail já cadastrado. Cadastre-se com outro e-mail!')

class FormLogin(FlaskForm):
    email = StringField ('E-mail', validators=[DataRequired(), Email()])
    senha = PasswordField ('Senha', validators=[DataRequired(), Length(6,20)])
    lembrar_dados = BooleanField('Lembrar')
    botao_entrar = SubmitField ('Entrar')

class FormEditarPerfil(FlaskForm):
    username = StringField ('Nome de Usuário', validators=[DataRequired()])
    email = StringField ('E-mail', validators=[DataRequired(), Email()])
    foto_perfil = FileField('Atualizar Foto de Perfil', validators=[FileAllowed(['jpg','png'])])

    curso_python = BooleanField('Curso de Python')
    curso_powerbi = BooleanField('Curso de Power BI')
    curso_excel = BooleanField('Curso de Excel')
    curso_sql = BooleanField('Curso de SQL')

    botao_editar = SubmitField ('Confirmar Edição')

    def validate_email(self, email):
        #verificar se o cara mudou de e-mail
        if current_user.email != email.data:
            usuario = Usuario.query.filter_by(email=email.data).first()
            if usuario:
                raise ValidationError('E-mail já cadastrado. Cadastre-se com outro e-mail!')