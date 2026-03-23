import mysql.connector
def get_connection():

    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="puntoventa",
        auth_plugin="mysql_native_password" 
    )

# SOLO para FastAPI Depends
def get_db():

    conn = get_connection()
    try:
        yield conn
    finally:
        conn.close()
