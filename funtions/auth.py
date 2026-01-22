from config.database import get_connection

def get_user_by_username(username: str):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute(
        "SELECT * FROM usuarios WHERE username = %s",
        (username,)
    )

    user = cursor.fetchone()

    cursor.close()
    conn.close()

    return user
