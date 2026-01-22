import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Admin",
        database="rrhh"
    )

# SOLO para FastAPI Depends (si luego lo necesitas)
def get_db():
    conn = get_connection()
    try:
        yield conn
    finally:
        conn.close()