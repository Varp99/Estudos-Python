from lib2to3.pgen2 import token
from flask import Flask, render_template, url_for

app = Flask(__name__)

lista_usuarios = ['Lira','João']
#Token de segurança para formulários
app.config['SECRET_KEY'] = 'c094b01296fb687d2cd30a591d226ef9'

@app.route("/")  #Caminho da nossa página
def home():
    return render_template('home.html') #Retorna e renderiza a página home que fica dentro da pasta templates

@app.route("/contato")
def contato():
    return render_template('contato.html')

@app.route("/usuarios")
def usuarios():
    return render_template('usuarios.html', lista_usuarios = lista_usuarios) #Coloca a lista de usuarios como parâmetro aqui para poder chamar ela na página usuarios.html

@app.route("/login")
def login():
    return render_template('login.html')

@app.route("/criarconta")
def criar_conta():
    return render_template('criarconta.html')

if __name__ == '__main__':
    app.run(debug=True)