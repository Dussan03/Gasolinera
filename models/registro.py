from models.database import Database
from datetime import datetime
import mysql.connector

class Registro:
    @staticmethod
    def verificar_uso_diario(cliente_id):
        db = Database()
        try:
            hoy = datetime.now().date()
            cursor = db.execute_query(
                "SELECT id FROM registros WHERE cliente_id = %s AND fecha = %s",
                (cliente_id, hoy))
            return cursor.fetchone() is not None
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
        except mysql.connector.Error as err:
            print(f"Error al registrar uso: {err}")
            return False
        finally:
            db.close()

    @staticmethod
    def obtener_todos_registros():
        db = Database()
        try:
            cursor = db.execute_query("""
                SELECT c.ci, c.nombre, c.apellido, r.fecha 
                FROM registros r
                JOIN clientes c ON r.cliente_id = c.id
                ORDER BY r.fecha DESC
            """)
            return cursor.fetchall()
        finally:
            db.close()