from flask import Blueprint, render_template, request, redirect, url_for
from models.cliente import Cliente

cliente_bp = Blueprint('cliente', __name__)

@cliente_bp.route('/registrar', methods=['GET', 'POST'])
def registrar():
    if request.method == 'POST':
        ci = request.form['ci']
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        
        if not Cliente.existe_ci(ci):
            Cliente.crear(ci, nombre, apellido)
            return redirect(url_for('index'))
        
        return "El cliente ya existe", 400
    
    return render_template('registro.html')