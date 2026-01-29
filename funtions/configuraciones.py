from fastapi import HTTPException

def obtener_permisos(db):
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM permisos")
    return cursor.fetchall()

def obtener_permisosbyuser(db,idUsuario):
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM usuarios_permisos where usuario_id = %s",
    (idUsuario,))
    return cursor.fetchall()


def agregar_permisosbyuser(db,idUsuario,idPermiso):
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM usuarios_permisos where usuario_id = %s AND permiso_id = %s",
    (idUsuario,idPermiso))
    if cursor.fetchone():
        return {"message": "El permiso ya está asignado"}
    
    cursor.execute("""
        INSERT INTO usuarios_permisos (usuario_id, permiso_id)
        VALUES (%s, %s)
    """, (idUsuario,idPermiso))

    db.commit()

    return {"message": "Permiso asignado correctamente"}

def eliminar_permisosbyuser(db,idUsuario,idPermiso):
    cursor = db.cursor(dictionary=True)
    cursor.execute("""
        DELETE FROM usuarios_permisos
        WHERE usuario_id = %s AND permiso_id = %s
    """, (idUsuario,idPermiso))

    db.commit()
    if cursor.rowcount == 0:
        raise HTTPException(status_code=404, detail="Permiso no encontrado")

    return {"message": "Permiso eliminado correctamente"}