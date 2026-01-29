from config.database import get_connection

def obtener_usuarios(db):
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM usuarios_con_empresaa")
    return cursor.fetchall()


def obtener_usuario_por_id(db, usuario_id: int):
    cursor = db.cursor(dictionary=True)

    cursor.execute(
        """
        SELECT 
            *
        FROM usuarios_con_empresaa
        WHERE id = %s
        """,
        (usuario_id,)
    )

    usuario = cursor.fetchone()

    cursor.close()
    db.close()
    return usuario


def crear_usuario(
        db, usuario, usuario_id, usuario_nombre,empresaId):
    cursor = db.cursor()
    forePasswordCange = 1
    estadoEmpleado = "Activo"

    cursor.execute(
        """
        INSERT INTO usuarios (username, password, role,createdByName,createdById,empresaId,Nombre,Correo,estado,forcePasswordChange,foto)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """,
        (
            usuario["username"], 
            usuario["password"], 
            usuario["rol"], 
            usuario_nombre, 
            usuario_id,
            empresaId,
            usuario["nombre"],
            usuario["Correo"],
            estadoEmpleado,
            forePasswordCange,
            usuario["foto"]
        )
    )
    db.commit()
    cursor.close()
    db.close()


def editar_usuario_sin_password(
    user_id: int,
    username: str,
    rol: str,
    empresaId: int
):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        UPDATE usuarios
        SET 
            username = %s,
            role = %s,
            empresaId = %s
        WHERE id = %s
        """,
        (username, rol, empresaId, user_id)
    )

    conn.commit()
    cursor.close()
    conn.close()