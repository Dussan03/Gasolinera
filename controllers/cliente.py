from flask import Blueprint, render_template, request, redirect, url_for, flash
from models.cliente import Cliente

cliente_bp = Blueprint('cliente', __name__)

@cliente_bp.route('/registrar', methods=['GET', 'POST'])
def registrar():
    if request.method == 'POST':
        ci = request.form['ci']
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        
        if not Cliente.existe_ci(ci):
            if Cliente.crear(ci, nombre, apellido):
                flash('Cliente registrado exitosamente', 'success')
                return redirect(url_for('cliente.registrar'))
            else:
                flash('Error al registrar cliente', 'error')
        else:
            flash('El cliente ya existe', 'warning')
    
    return render_template('registro.html')