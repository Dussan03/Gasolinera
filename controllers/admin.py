from flask import Blueprint, render_template
from models.registro import Registro

admin_bp = Blueprint('admin', __name__)

@admin_bp.route('/admin')
def panel_admin():
    registros = Registro.obtener_todos_registros()
    return render_template('admin.html', registros=registros)