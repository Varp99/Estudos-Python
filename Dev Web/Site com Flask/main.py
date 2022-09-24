from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")  #Caminho da nossa página
def home():
    return render_template('home.html') #Retorna e renderiza a página home que fica dentro da pasta templates

@app.route("/contato")
def contato():
    return render_template('contato.html')

if __name__ == '__main__':
    app.run(debug=True)