from config.database import get_connection

def crear_usuario(username: str, password: str, rol: str):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO usuarios (username, password, role)
        VALUES (%s, %s, %s)
        """,
        (username, password, rol)
    )

    conn.commit()
    cursor.close()
    conn.close()
