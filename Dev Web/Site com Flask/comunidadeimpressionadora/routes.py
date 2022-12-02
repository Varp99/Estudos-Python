#AQUI É A PARTE ONDE CRIA TODAS AS FUNÇÕES DE PÁGINAS

from flask import render_template, redirect, url_for, flash, request
from comunidadeimpressionadora import app, database, bcrypt
from comunidadeimpressionadora.forms import FormLogin, FormCriarConta, FormEditarPerfil
from comunidadeimpressionadora.models import Usuario
from flask_login import login_user, logout_user, current_user, login_required

lista_usuarios = ['Lira','João']

@app.route("/")  #Caminho da nossa página
def home():
    return render_template('home.html') #Retorna e renderiza a página home que fica dentro da pasta templates

@app.route("/contato")
def contato():
    return render_template('contato.html')

@app.route("/usuarios")
@login_required
def usuarios():
    return render_template('usuarios.html', lista_usuarios = lista_usuarios) #Coloca a lista de usuarios como parâmetro aqui para poder chamar ela na página usuarios.html

@app.route("/login", methods=['GET','POST']) #Toda página que tiver formulário tem que passar esse methods get e post.
def login():
    form_login = FormLogin()

    if form_login.validate_on_submit() and 'botao_entrar' in request.form: #Verifica se o formulário foi validado e se o botão que eu cliquei foi o de login
        #encontra o usuario
        usuario = Usuario.query.filter_by(email=form_login.email.data).first()
        #Se o usuario existe e a senha do banco de dados é a mesma que ele preencheu no formulário então funciona o login
        if usuario and bcrypt.check_password_hash(usuario.senha, form_login.senha.data):
            #Faz o login efetivamente
            login_user(usuario, remember=form_login.lembrar_dados.data)
            #Exibe mensagem de sucesso
            flash(f'Login feito com sucesso no e-mail: {form_login.email.data}', 'alert-success')
            #Pega o parâmetro next e verifica se ele existe, para redirecionar pra página que o usuário queria ir
            par_next = request.args.get('next')
            if par_next:
                return redirect(par_next)
            else:
                #Redireciona para tal página
                return redirect(url_for('home'))
        else:
            #Exibe mensagem de erro
            flash(f'Falha no Login. E-mail ou Senha incorretos', 'alert-danger')
        
    
    return render_template('login.html', form_login = form_login)

@app.route("/criarconta", methods=['GET','POST'])#Toda página que tiver formulário tem que passar esse methods get e post.
def criar_conta():
    form_criarconta = FormCriarConta()

    if form_criarconta.validate_on_submit() and 'botao_criar' in request.form: #Verifica se o formulário foi validado e se o botão que eu cliquei foi o de criar conta
        #Transforma a senha em criptografia
        senha_cript = bcrypt.generate_password_hash(form_criarconta.senha.data)
        #Estamos criando um usuário no banco de dados
        usuario = Usuario(username=form_criarconta.username.data, email=form_criarconta.email.data, senha=senha_cript)
        #Estamos adicionando o usuário na sessão do banco de dados
        database.session.add(usuario)
        #Estamos dando um commit
        database.session.commit()
        #Exibir mensagem
        flash(f'Conta criada com sucesso no e-mail: {form_criarconta.email.data}', 'alert-success')
        #Redireciona para tal página
        return redirect(url_for('home'))

    return render_template('criarconta.html', form_criarconta = form_criarconta)

#Faz o logout e redireciona pra home
@app.route('/sair')
@login_required
def sair():
    logout_user()
    flash(f'Logout feito com sucesso!!', 'alert-success')
    return redirect(url_for('home'))

@app.route('/perfil')
#Esse login required serve para bloquear a página pra pessoa, ou seja ela só consegue ver se estiver logada
@login_required
def perfil():
    foto_perfil = url_for('static', filename='fotos_perfil/{}'.format(current_user.foto_perfil))
    return render_template('perfil.html', foto_perfil=foto_perfil)

@app.route('/post/criar')
@login_required
def criar_post():
    return render_template('criarpost.html')

@app.route('/perfil/editar', methods=['GET','POST'])
@login_required
def editar_perfil():
    form = FormEditarPerfil()

    if form.validate_on_submit():
        current_user.email = form.email.data
        current_user.username = form.username.data
        database.session.commit()
        flash(f'Perfil atualizado com sucesso', 'alert-success')
        return redirect(url_for('perfil'))
    #Carrega as informações nos campos de editar perfil
    elif request.method == "GET":
        form.email.data = current_user.email
        form.username.data = current_user.username

    foto_perfil = url_for('static', filename='fotos_perfil/{}'.format(current_user.foto_perfil))
    return render_template('editarperfil.html', foto_perfil=foto_perfil, form=form)