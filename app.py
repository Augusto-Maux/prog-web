from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime # IMPORTAÇÃO

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

@app.route('/dados')
def dados():
    return render_template('formulario.html')

@app.route('/recebedados', methods=['GET', 'POST'])
def recebedados():
    nome = request.args.get("nome")
    email = request.args.get("email")
    nome_post = request.form["nome"]
    email_post = request.form["email"]
    estado = request.form["estado"]
    formacao = request.form["formacao"]
    modalidades = request.form.getlist("modalidades")
    data_nasc = request.form["data"]
    data_obj = datetime.strptime(data_nasc, "%Y-%m-%d")
    data_nasc_br = data_obj.strftime("%d/%m/%Y")

    return f"{nome_post} - {email_post} - {estado} - {formacao} - {modalidades} - {data_nasc_br}"



@app.route('/verificaridade/<int:idade>')
def verificaridade(idade):
    return render_template('verificaridade.html', idade=idade)

@app.route('/situacaofinal/<float:nota>')
def situacao_final(nota):
    if nota >= 6:
        return 'Aprovado'
    
    elif nota >= 3:
        return 'Recuperação'

    else:
        return 'Reprovado'

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/verificarlogin', methods=['POST'])
def verificarlogin():

    if request.method == 'POST':
        login = request.form['login']
        senha = request.form['senha']

        if login == 'admin' and senha == '12345':
            return redirect(url_for('index'))
        else:
            return 'Sem permissão'

@app.route('/numero/<int:n>')
def numero(n):
	return render_template('numero.html', n=n)

@app.route('/escolheritens')
def escolheritens():
	return render_template('escolheritens.html')

@app.route('/compras')
def compras():
	itens = request.args.getlist("itens")
	return render_template('compras.html', itens=itens)

@app.route('/contatos')
def contatos():
	dados = [
			{'nome':'Alba', 'telefone':'9999-8888'},
			{'nome':'Maria', 'telefone':'7777-6666'},
			{'nome':'Carla', 'telefone':'5555-4444'}
	]
	return render_template('contatos.html', dados=dados)

if __name__ == '__main__':
    app.run(debug=True)