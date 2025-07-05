from datetime import datetime
from models.database import Database

class Registro:
    @staticmethod
    def registrar_cliente(cliente_id, vehiculo_id):
        db = Database()
        try:
            semana_actual = datetime.now().isocalendar()[1]
            db.execute_query(
                "INSERT INTO registros (cliente_id, vehiculo_id, semana) VALUES (%s, %s, %s)",
                (cliente_id, vehiculo_id, semana_actual)
            )
            return True
        except Exception as e:
            print(f"Error al registrar cliente: {e}")
            return False
        finally:
            db.close()

    @staticmethod
    def marcar_uso(cliente_id):
        db = Database()
        try:
            semana_actual = datetime.now().isocalendar()[1]
            
            # Verificar límite de 2 cargas por semana
            cursor = db.execute_query(
                "SELECT contador_semana FROM registros WHERE cliente_id = %s AND semana = %s",
                (cliente_id, semana_actual)
            )
            registro = cursor.fetchone()
            
            if registro and registro['contador_semana'] >= 2:
                return False, "Límite de cargas alcanzado esta semana"
            
            # Actualizar registro
            db.execute_query(
                """UPDATE registros 
                SET usado = TRUE, 
                    contador_semana = contador_semana + 1 
                WHERE cliente_id = %s AND semana = %s""",
                (cliente_id, semana_actual)
            )
            return True, "Carga registrada exitosamente"
        except Exception as e:
            print(f"Error al marcar uso: {e}")
            return False, str(e)
        finally:
            db.close()

    @staticmethod
    def obtener_historial(cliente_id):
        db = Database()
        try:
            # Usamos fetch=True para obtener todos los resultados inmediatamente
            return db.execute_query(
                """SELECT r.*, v.placa, v.marca, v.modelo 
                FROM registros r
                JOIN vehiculos v ON r.vehiculo_id = v.id
                WHERE r.cliente_id = %s
                ORDER BY r.fecha DESC""",
                (cliente_id,), 
                fetch=True
            )
        except Exception as e:
            print(f"Error al obtener historial: {e}")
            return []
        finally:
            db.close()