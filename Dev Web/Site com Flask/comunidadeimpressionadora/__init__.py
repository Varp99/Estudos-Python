# ISSO AQUI TUDO FAZ PARTE DA CONFIGURAÇÃO DO SITE E INICIALIZA O SITE
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)

#Token de segurança para formulários
app.config['SECRET_KEY'] = 'c094b01296fb687d2cd30a591d226ef9'
#Caminho do banco de dados que o sql alchemy vai controlar
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///projeto.db'

#Vai criar o banco de dados usando essa classe SQLAlchemy de acordo com as config do app
database = SQLAlchemy(app)
#Criptografia
bcrypt = Bcrypt(app)
#Variavel do login manager
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message = 'Por favor, faça login para acessar essa página.'
login_manager.login_message_category = 'alert-info'

from comunidadeimpressionadora import routes  #Tem que ser aqui embaixo essa importação pq ele precisa do app