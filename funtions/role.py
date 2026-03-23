from config.database import get_connection

# ---------------- CREAR ROL ----------------
def crear_rol(db, rol: dict):
    cursor = db.cursor()
    # Insertar rol
    cursor.execute("INSERT INTO roles (name) VALUES (%s)", (rol["name"],))
    db.commit()
    role_id = cursor.lastrowid

    # Insertar permisos
    permisos = rol.get("permisos", [])
    for permiso_name in permisos:
        cursor.execute("SELECT id FROM permissions WHERE name = %s", (permiso_name,))
        permiso_row = cursor.fetchone()
        if permiso_row:
            permission_id = permiso_row[0]
            cursor.execute(
                "INSERT INTO role_permissions (role_id, permission_id) VALUES (%s, %s)",
                (role_id, permission_id)
            )
    db.commit()
    cursor.close()
    db.close()


# ---------------- EDITAR ROL ----------------
def editar_rol(db, role_id: int, rol: dict):
    cursor = db.cursor()
    # Actualizar nombre del rol
    cursor.execute("UPDATE roles SET name = %s WHERE id = %s", (rol["name"], role_id))
    
    # Borrar permisos antiguos
    cursor.execute("DELETE FROM role_permissions WHERE role_id = %s", (role_id,))
    
    # Insertar permisos nuevos (usar permission_id en lugar de nombre)
    permisos = rol.get("permisos", [])
    for permiso_name in permisos:
        # Obtener id del permiso
        cursor.execute("SELECT id FROM permissions WHERE name = %s", (permiso_name,))
        permiso_row = cursor.fetchone()
        if permiso_row:
            permission_id = permiso_row[0]
            cursor.execute(
                "INSERT INTO role_permissions (role_id, permission_id) VALUES (%s, %s)",
                (role_id, permission_id)
            )
    
    db.commit()
    cursor.close()
    db.close()


# ---------------- ELIMINAR ROL ----------------
def eliminar_rol(db, role_id: int):
    cursor = db.cursor()
    # Borrar permisos asociados
    cursor.execute("DELETE FROM role_permissions WHERE role_id = %s", (role_id,))
    # Borrar rol
    cursor.execute("DELETE FROM roles WHERE id = %s", (role_id,))
    db.commit()
    cursor.close()
    db.close()


# ---------------- OBTENER ROLES CON PERMISOS ----------------
def obtener_roles(db):
    cursor = db.cursor(dictionary=True)
    cursor.execute("""
        SELECT r.id, r.name, p.name AS permiso
        FROM roles r
        LEFT JOIN role_permissions rp ON r.id = rp.role_id
        LEFT JOIN permissions p ON rp.permission_id = p.id
        ORDER BY r.id
    """)
    rows = cursor.fetchall()

    roles = {}
    for row in rows:
        role_id = row["id"]
        if role_id not in roles:
            roles[role_id] = {
                "id": role_id,
                "name": row["name"],
                "permisos": []
            }
        if row["permiso"]:
            roles[role_id]["permisos"].append(row["permiso"])

    cursor.close()
    db.close()
    return list(roles.values())