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
            print("Ejecutando consulta de registros...")  # Debug
            query = """
                SELECT 
                    c.ci AS ci, 
                    c.nombre AS nombre, 
                    c.apellido AS apellido, 
                    r.fecha AS fecha
                FROM registros r
                JOIN clientes c ON r.cliente_id = c.id
                ORDER BY r.fecha DESC
            """
            registros = db.execute_query(query, fetch=True)
            print(f"Registros obtenidos: {registros}")  # Debug
            return registros if registros else [] 
        except Exception as e:
            print(f"Error al obtener registros: {str(e)}")  # Debug detallado
            return []
        finally:
            db.close()