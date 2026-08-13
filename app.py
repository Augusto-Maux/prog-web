# app.py
import os
from flask import Flask, render_template
from flask_migrate import Migrate
from utils import db
from models import Usuario, Pizza, Pedido
from controllers.Usuario import bp_usuario 

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
db_username = os.getenv('DB_USERNAME') or 'root'
db_password = os.getenv('DB_PASSWORD') or ''
db_host = os.getenv('DB_HOST') or '127.0.0.1'
db_database = os.getenv('DB_DATABASE') or 'fases.tech'
db_port = os.getenv('DB_PORT') or '3306'
conexao = f"mysql+pymysql://{db_username}:{db_password}@{db_host}:{db_port}/{db_database}"
app.config["SQLALCHEMY_DATABASE_URI"] = conexao
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)

# Registrando o Blueprint correto
app.register_blueprint(bp_usuario, url_prefix='/usuarios')

@app.route('/')
def inicial():
    return render_template('inicial.html')
 
@app.route("/teste_insert")
def teste_insert():
    pizza = Pizza("Calabresa", 70.0)
    db.session.add(pizza)
    db.session.commit()	
    return "Dados inseridos!"	

@app.route("/teste_select")
def teste_select():
    p = Pizza.query.get(1)
    return p.nome if p else "Nenhuma pizza encontrada"

@app.route("/teste_update")
def teste_update():
    user = Pizza.query.get(1)
    if user:
        user.nome = '4 Queijos'
    else:
        return 'Pizza não encontrada'
    db.session.add(user)
    db.session.commit()
    return 'Dados atualizados'

@app.route("/teste_delete")
def teste_delete():		
    p = Pizza.query.get(1)
    if p:
        db.session.delete(p)
        db.session.commit()
        return 'Dados excluídos'
    return 'Pizza não encontrada'

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
