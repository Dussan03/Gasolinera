import mysql.connector
from config import DB_CONFIG

class Database:
    def __init__(self):
        self.connection = mysql.connector.connect(**DB_CONFIG)
        self.cursor = self.connection.cursor(dictionary=True, buffered=True)
    
    def execute_query(self, query, params=None, fetch=False):
        try:
            self.cursor.execute(query, params or ())
            
            if fetch:
                result = self.cursor.fetchall()
                # Limpiar cualquier resultado adicional
                while self.cursor.nextset():
                    pass
                return result
            return True
            
        except mysql.connector.Error as err:
            print(f"Database error: {err}")
            raise
        finally:
            self.connection.commit()
    
    def fetch_one(self, query, params=None):
        try:
            self.cursor.execute(query, params or ())
            result = self.cursor.fetchone()
            # Limpiar resultados pendientes
            while self.cursor.nextset():
                pass
            return result
        except mysql.connector.Error as err:
            print(f"Database error: {err}")
            raise
    
    def close(self):
        try:
            # Limpiar cualquier resultado pendiente
            while self.cursor.nextset():
                pass
        except:
            pass
        finally:
            self.cursor.close()
            self.connection.close()

    def create_tables(self):
        # Tabla de clientes
        self.execute_query("""
            CREATE TABLE IF NOT EXISTS clientes (
                id INT AUTO_INCREMENT PRIMARY KEY,
                ci VARCHAR(20) UNIQUE NOT NULL,
                nombre VARCHAR(100) NOT NULL,
                apellido VARCHAR(100) NOT NULL
            )
        """)
        
        # Tabla de vehículos
        self.execute_query("""
            CREATE TABLE IF NOT EXISTS vehiculos (
                id INT AUTO_INCREMENT PRIMARY KEY,
                cliente_id INT NOT NULL,
                chasis VARCHAR(50) UNIQUE NOT NULL,
                placa VARCHAR(20) NOT NULL UNIQUE,
                marca VARCHAR(50) NOT NULL,
                modelo VARCHAR(50) NOT NULL,
                FOREIGN KEY (cliente_id) REFERENCES clientes(id)
            )
        """)
        
        # Tabla de registros de servicio
        self.execute_query("""
            CREATE TABLE IF NOT EXISTS registros (
                id INT AUTO_INCREMENT PRIMARY KEY,
                cliente_id INT,
                fecha DATE,
                FOREIGN KEY (cliente_id) REFERENCES clientes(id),
                UNIQUE (cliente_id, fecha) -- evita más de un uso por día
            )
        """)