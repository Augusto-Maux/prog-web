# controllers/Usuario.py
from flask import render_template, Blueprint
from models import Usuario
from utils import db

bp_usuario = Blueprint("usuario", __name__, template_folder="templates")

@bp_usuario.route('/recovery')
def recovery():
    return render_template('usuarios_recovery.html')