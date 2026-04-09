from flask import Flask, render_template # IMPORTAÇÃO

app = Flask(__name__) # INSTÂNCIA DA CLASSE FLASK

@app.route('/')
def index():
    return render_template('index.html')

# @app.route('/fale-conosco') -> POR ISSO É MELHOR USAR {{ url_for(função) }}, POIS HÁ DIFERENTES ROTAS PARA MESMA FUNÇÃO
@app.route('/contato')
def contato():
    # return render_template('contato.html', tel = '(84) 99233-2910', email = 'augusto.maux@escolar.ifrn.edu.br', nome = 'Augusto Maux')

    # nome = "Augusto"
    # email = "augusto.maux@escolar.ifrn.edu.br"
    # tel = '(84) 99233-2910'
    # return render_template('contato.html', nome = nome, email = email, tel = tel)

    dados = { "nome" : "Augusto Maux", "email" : "augusto.maux@escolar.ifrn.edu.br", "tel" : "(84) 99233-2910" }
    return render_template('contato.html', dados = dados)

@app.route('/usuario', defaults = {"nome" : "Desconhecido", "sobrenome" : "Desconhecido"})
@app.route('/usuario/<nome>/<sobrenome>')
def usuario(nome, sobrenome):
    info = { "nome" : nome, "sobrenome" : sobrenome }
    return render_template('usuario.html', info = info)
    
# @app.route('/user', defaults = {"nome" : "Desconhecido"})
@app.route('/user/<nome>')
def user(nome):
    return render_template('user.html', nome = nome)

@app.route('/semestre/<int:x>')
def semestre(x):
    # data = { "atual" : x, "anterior" : x - 1 }
    data = {}
    data["atual"] = x
    data["anterior"] = x - 1
    return render_template('semestre.html', data = data)

if __name__ == '__main__':
    app.run(debug=True)