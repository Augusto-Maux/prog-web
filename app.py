from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime # IMPORTAÇÃO

from utils import db
import os
from flask_migrate import Migrate
from models import Usuario


app = Flask(__name__) # INSTÂNCIA DA CLASSE FLASK
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
db_username = os.getenv('DB_USERNAME')
db_password = os.getenv('DB_PASSWORD')
db_host = os.getenv('DB_HOST')
db_database = os.getenv('DB_DATABASE')
db_port = os.getenv('DB_PORT')

conexao = f"mysql+pymysql://{db_username}:{db_password}@{db_host}:{db_port}/{db_database}"
app.config["SQLALCHEMY_DATABASE_URI"] = conexao
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

migrate = Migrate(app, db)

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