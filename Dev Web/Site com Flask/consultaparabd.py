from turtle import pos
from main import app, database
from models import Usuario, Post

with app.app_context():
    database.drop_all()
    database.create_all()


#Cria um novo usuario no banco de dados
#with app.app_context():
 #   usuario = Usuario(username="Vini", email="vini.arpini@hotmail.com", senha="123456")
  #  database.session.add(usuario)
  #  database.session.commit()

#Busca usuarios no banco de dados
#with app.app_context():
    #meus_usuarios = Usuario.query.all()
    #print(meus_usuarios)
    #primeiro_usuario = Usuario.query.first()
    #print(primeiro_usuario.id)
    #print(primeiro_usuario.email)

#Cria um post
# with app.app_context():
#     meu_post = Post(id_usuario=1, titulo="Primeiro Post", corpo="Vini voando")
#     database.session.add(meu_post)
#     database.session.commit()

#Busca um Post no banco de dados
# with app.app_context():
#     post = Post.query.first()
#     print(post.titulo)
#     print(post.autor.email)