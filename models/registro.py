from models.database import Database
from datetime import datetime

class Registro:
    @staticmethod
    def verificar_uso_diario(cliente_id):
        db = Database()
        try:
            hoy = datetime.now().date()
            return db.fetch_one(
                "SELECT id FROM registros WHERE cliente_id = %s AND fecha = %s",
                (cliente_id, hoy))
        finally:
            db.close()

    @staticmethod
    def registrar_uso(cliente_id):
        db = Database()
        try:
            hoy = datetime.now().date()
            db.execute_query(
                "INSERT INTO registros (cliente_id, fecha) VALUES (%s, %s)",
                (cliente_id, hoy))
            return True
        except Exception as err:
            print(f"Error al registrar uso: {err}")
            return False
        finally:
            db.close()

    @staticmethod
    def obtener_todos_registros():
        db = Database()
        try:
            connection = db.connection
            if not connection.is_connected():
                connection.ping(reconnect=True, attempts=3, delay=5)
            with connection.cursor(dictionary=True) as cursor:
                print("Ejecutando consulta de registros...")
                cursor.execute("""
                SELECT 
                    c.ci AS ci, 
                    c.nombre AS nombre, 
                    c.apellido AS apellido, 
                    r.fecha AS fecha
                FROM registros r
                JOIN clientes c ON r.cliente_id = c.id
                ORDER BY r.fecha DESC
                """)
                registros = cursor.fetchall()  # <--- muy importante
                connection.close()
            return registros
        except Exception as e:
            print("Error al obtener registros:", e)
            return []
        finally:
            db.close()