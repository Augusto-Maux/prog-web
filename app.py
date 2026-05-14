from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime # IMPORTAÇÃO

app = Flask(__name__) # INSTÂNCIA DA CLASSE FLASK

@app.route('/<int:qtd>')
def index(qtd):
    return render_template('index.html', qtd=qtd)


if __name__ == '__main__':
    app.run(debug=True)