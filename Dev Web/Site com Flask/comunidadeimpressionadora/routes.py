#AQUI É A PARTE ONDE CRIA TODAS AS FUNÇÕES DE PÁGINAS

from flask import render_template, redirect, url_for, flash, request
from comunidadeimpressionadora import app
from comunidadeimpressionadora.forms import FormLogin, FormCriarConta

lista_usuarios = ['Lira','João']

@app.route("/")  #Caminho da nossa página
def home():
    return render_template('home.html') #Retorna e renderiza a página home que fica dentro da pasta templates

@app.route("/contato")
def contato():
    return render_template('contato.html')

@app.route("/usuarios")
def usuarios():
    return render_template('usuarios.html', lista_usuarios = lista_usuarios) #Coloca a lista de usuarios como parâmetro aqui para poder chamar ela na página usuarios.html

@app.route("/login", methods=['GET','POST']) #Toda página que tiver formulário tem que passar esse methods get e post.
def login():
    form_login = FormLogin()

    if form_login.validate_on_submit() and 'botao_entrar' in request.form: #Verifica se o formulário foi validado e se o botão que eu cliquei foi o de login
        #Exibir mensagem
        flash(f'Login feito com sucesso no e-mail: {form_login.email.data}', 'alert-success')
        #Redireciona para tal página
        return redirect(url_for('home'))
    
    return render_template('login.html', form_login = form_login)

@app.route("/criarconta", methods=['GET','POST'])#Toda página que tiver formulário tem que passar esse methods get e post.
def criar_conta():
    form_criarconta = FormCriarConta()

    if form_criarconta.validate_on_submit() and 'botao_criar' in request.form: #Verifica se o formulário foi validado e se o botão que eu cliquei foi o de criar conta
        #Exibir mensagem
        flash(f'Conta criada com sucesso no e-mail: {form_criarconta.email.data}', 'alert-success')
        #Redireciona para tal página
        return redirect(url_for('home'))

    return render_template('criarconta.html', form_criarconta = form_criarconta)