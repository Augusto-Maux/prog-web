from flask import Flask, render_template # IMPORTAÇÃO

app = Flask(__name__) # INSTÂNCIA DA CLASSE FLASK

@app.route('/')
def index():
    return render_template('index.html')

# @app.route('/fale-conosco') -> POR ISSO É MELHOR USAR {{ url_for(função) }}, POIS HÁ DIFERENTES ROTAS PARA MESMA FUNÇÃO
@app.route('/contato')
def contato():
    return render_template('contato.html')

if __name__ == '__main__':
    app.run(debug=True)