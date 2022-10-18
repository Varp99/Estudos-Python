#Banco de dados

from main import database #importando nosso database do arquivo main
from datetime import datetime #importar pra poder pegar a data do momento atual

class Usuario(database.Model):
    id = database.Column(database.Integer, primary_key = True) #Coluna ID do tipo inteiro e chave primária
    username = database.Column(database.String, nullable = False) #Coluna de usuário do tipo String (texto) nenhum usuário consegue criar uma conta sem dizer o nome do usuário
    email = database.Column(database.String, nullable = False, unique = True) #Esse unique significa que nenhum usuário pode ter o mesmo email no banco de dados
    senha = database.Column(database.String, nullable = False)
    foto_perfil = database.Column(database.String, default = 'default.jpg') #Se o cara não preencher a foto carrega essa foto padrão
    posts = database.relationship('Post', backref = 'autor', lazy = True) #Essa parte não é uma tabela, é um relacionamento
    cursos = database.Column(database.String, nullable = False, default = 'Não informado')

class Post(database.Model):
    id = database.Column(database.Integer, primary_key = True)
    titulo = database.Column(database.String, nullable = False)
    corpo = database.Column(database.Text, nullable = False) #Definido como TEXT pq são textos maiores
    data_criacao = database.Column(database.DateTime, nullable = False, default = datetime.utcnow) #Datetime salva com a data do momento em que a pessoa faz o post
    id_usuario = database.Column(database.Integer, database.ForeignKey('usuario.id'), nullable = False)