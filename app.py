from flask import Flask # IMPORTAÇÃO

app = Flask(__name__) # INSTÂNCIA DA CLASSE FLASK

@app.route('/')
def index():
    return 'Olá Mundo!'

@app.route('/contato')
def contato():
    return 'augusto.maux@escolar.ifrn.edu.br'