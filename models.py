from utils import db

class Usuario(db.Model):
	__tablename__= "usuario"
	id = db.Column(db.Integer, primary_key = True)
	nome = db.Column(db.String(100))
	email = db.Column(db.String(100))
	senha = db.Column(db.String(100))
	
	def __init__(self, nome, email, senha):
		self.nome = nome
		self.email = email
		self.senha = senha
		
	def __repr__(self):
		return "<Usuario {}>".format(self.nome)
	
class Pizza(db.Model):
	__tablename__= "pizza"
	id = db.Column(db.Integer, primary_key = True)
	sabor = db.Column(db.String(100))
	imagem = db.Column(db.String(100))
	ingredientes = db.Column(db.String(100))
	precos = db.Column(db.Numeric(10, 2))

	def __init__(self, sabor, precos):
		self.sabor = sabor
		self.precos = precos
		
	def __repr__(self):
		return "<Pizza {}>".format(self.sabor)

class Pedido(db.Model):
	
	__tablename__= "pedido"
	id = db.Column(db.Integer, primary_key = True)
	nome = db.Column(db.String(100))
	id_usuario = db.Column(db.Integer, db.ForeignKey(Usuario.id), primary_key=True)
	id_pizza = db.Column(db.Integer, db.ForeignKey(Usuario.id), primary_key=True)
	data = db.Column(db.Date)

	def __init__(self, nome, id_usuario, id_pizza):
		self.nome = nome
		self.id_usuario = id_usuario
		self.id_pizza = id_pizza
		
	def __repr__(self):
		return "<Pedido {}>".format(self.id)