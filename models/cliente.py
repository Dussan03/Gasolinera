import mysql.connector
from models.database import Database

class Cliente:
    @staticmethod
    def crear(ci, nombre, apellido):
        db = Database()
        try:
            db.execute_query(
                "INSERT INTO clientes (ci, nombre, apellido) VALUES (%s, %s, %s)",
                (ci, nombre, apellido)
            )
            return True
        except mysql.connector.Error as err:
            print(f"Error al crear cliente: {err}")
            return False
        finally:
            db.close()

    @staticmethod
    def existe_ci(ci):
        db = Database()
        try:
            resultado = db.fetch_one("SELECT id FROM clientes WHERE ci = %s", (ci,))
            return resultado is not None
        finally:
            db.close()

    @staticmethod
    def obtener_por_ci(ci):
        db = Database()
        try:
            return db.fetch_one(
                "SELECT id, ci, nombre, apellido FROM clientes WHERE ci = %s",
                (ci,))
        finally:
            db.close()