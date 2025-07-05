from flask import Blueprint, render_template, request, flash
from models.cliente import Cliente
from models.registro import Registro

verificacion_bp = Blueprint('verificacion', __name__)

@verificacion_bp.route('/verificar', methods=['GET', 'POST'])
def verificar():
    if request.method == 'POST':
        ci = request.form['ci']
        accion = request.form.get('accion')
        
        try:
            cliente = Cliente.obtener_por_ci(ci)
            if not cliente:
                flash('Cliente no encontrado', 'error')
                return render_template('verificar.html')
            
            if accion == 'marcar_uso':
                success, mensaje = Registro.marcar_uso(cliente['id'])
                flash(mensaje, 'success' if success else 'error')
            
            # Obtenemos el historial de manera segura
            historial = Registro.obtener_historial(cliente['id']) or []
            return render_template('verificar.html', 
                                cliente=cliente, 
                                historial=historial)
            
        except Exception as e:
            print(f"Error en verificación: {e}")
            flash('Error al procesar la solicitud', 'error')
            return render_template('verificar.html')
    
    return render_template('verificar.html')