from config.database import get_connection

def obtener_usuarios(db):
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM usuarios")
    return cursor.fetchall()


def obtener_usuario_por_Username(db, usuarioName: str):
    cursor = db.cursor(dictionary=True)
    cursor.execute(
        """
        SELECT 
            *
        FROM usuarios
        WHERE username = %s
        """,
        (usuarioName,)
    )

    usuario = cursor.fetchone()
    cursor.close()
    db.close()
    return usuario

def obtener_usuario_por_id(db, usuario_id: int):
    cursor = db.cursor(dictionary=True)

    cursor.execute(
        """
        SELECT 
            *
        FROM usuarios
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

def editar_usuario(db, usuario_id: int, data: dict):
    cursor = db.cursor()

    campos = ", ".join([f"{k} = %s" for k in data.keys()])
    valores = list(data.values())
    valores.append(usuario_id)

    query = f"""
        UPDATE usuarios
        SET {campos}
        WHERE id = %s
    """

    cursor.execute(query, valores)
    db.commit()

def eliminar_usuario(db, usuario_id: int):
    cursor = db.cursor()

    cursor.execute(
        """
        Delete 
        FROM usuarios
        WHERE id = %s
        """,
        (usuario_id,)
    )

    cursor.execute(
        """
        DELETE FROM usuarios_permisos
        WHERE usuario_id = %s
        """,
        (usuario_id,)
    )
    
    db.commit()
    cursor.close()
    db.close()