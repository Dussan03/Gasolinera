from models.database import Database

def initialize_database():
    db = Database()
    try:
        db.create_tables()
        print("✅ Tablas creadas exitosamente")
    except Exception as e:
        print(f"❌ Error al crear tablas: {e}")
    finally:
        db.close()

if __name__ == "__main__":
    initialize_database()