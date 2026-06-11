from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime # IMPORTAÇÃO

app = Flask(__name__) # INSTÂNCIA DA CLASSE FLASK

@app.route('/')
def inicial():
    return render_template('inicial.html')

@app.route('/cardapio')
def cardapio():
	return render_template('cardapio.html')

@app.route('/avaliacoes')
def avaliacao():
	return render_template('avaliacao.html')

@app.route('/faleconosco')
def fale_conosco():
	return render_template('fale_conosco.html')

@app.route('/login')
def login():
	return render_template('login.html')
 

if __name__ == '__main__':
    app.run(debug=True)