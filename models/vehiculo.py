from models.database import Database

class Vehiculo:
    @staticmethod
    def crear(cliente_id, chasis, placa, marca, modelo):
        db = Database()
        try:
            cursor = db.execute_query(
                """INSERT INTO vehiculos 
                (cliente_id, chasis, placa, marca, modelo) 
                VALUES (%s, %s, %s, %s, %s)""",
                (cliente_id, chasis, placa, marca, modelo)
            )
            return cursor.lastrowid
        except Exception as e:
            print(f"Error al crear vehículo: {e}")
            return None
        finally:
            db.close()