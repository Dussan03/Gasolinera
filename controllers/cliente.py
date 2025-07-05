from flask import Blueprint, render_template, request, flash, redirect, url_for
from models.cliente import Cliente
from models.vehiculo import Vehiculo
from models.registro import Registro

cliente_bp = Blueprint('cliente', __name__)

@cliente_bp.route('/registrar', methods=['GET', 'POST'])
def registrar():
    if request.method == 'POST':
        # Datos del cliente
        ci = request.form['ci']
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        
        # Datos del vehículo
        chasis = request.form['chasis']
        placa = request.form['placa']
        marca = request.form['marca']
        modelo = request.form['modelo']

        if not Cliente.existe_ci(ci):
            cliente_id = Cliente.crear(ci, nombre, apellido)
            if cliente_id:
                vehiculo_id = Vehiculo.crear(cliente_id, chasis, placa, marca, modelo)
                if vehiculo_id:
                    if Registro.registrar_cliente(cliente_id, vehiculo_id):
                        flash('Cliente y vehículo registrados exitosamente', 'success')
                        return redirect(url_for('cliente.registrar'))
        
        flash('Error en el registro', 'error')
    
    return render_template('registro.html')