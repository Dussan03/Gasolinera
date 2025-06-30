from flask import Blueprint, render_template, request, flash
from models.cliente import Cliente
from models.registro import Registro

verificacion_bp = Blueprint('verificacion', __name__)

@verificacion_bp.route('/verificar', methods=['GET', 'POST'])
def verificar():
    if request.method == 'POST':
        ci = request.form['ci']
        cliente = Cliente.obtener_por_ci(ci)
        
        if not cliente:
            flash('Cliente no encontrado', 'error')
        else:
            if Registro.verificar_uso_diario(cliente['id']):
                flash('Este cliente ya usó el servicio hoy', 'warning')
            else:
                if Registro.registrar_uso(cliente['id']):
                    flash('Cliente verificado exitosamente', 'success')
                else:
                    flash('Error al registrar el uso', 'error')
        
        return render_template('verificar.html', cliente=cliente)
    
    return render_template('verificar.html')