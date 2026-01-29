def obtener_empleados(db):
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM empleados")
    return cursor.fetchall()


def obtener_empleado_por_id(db, empleado_id: int):
    cursor = db.cursor(dictionary=True)
    cursor.execute(
        "SELECT * FROM empleados WHERE id = %s",
        (empleado_id,)
    )
    return cursor.fetchone()

def insertar_empleado(db, empleado, usuario_id, usuario_nombre,empresaId):
    cursor = db.cursor()
    cursor.execute("""
        INSERT INTO empleados
        (nombre, departamento, puesto, salario, fecha_ingreso, estado, foto, created, createdById, createdByName,empresaId)
        VALUES (%s, %s, %s, %s, %s, %s, %s, NOW(), %s, %s, %s)
    """, (
        empleado["nombre"],
        empleado["departamento"],
        empleado["puesto"],
        empleado["salario"],
        empleado["fecha_ingreso"],
        empleado["estado"],
        empleado["foto"],
        usuario_id,
        usuario_nombre,
        empresaId
    ))
    db.commit()
    return cursor.lastrowid


def eliminar_empleado(db, empleado_id: int):
    cursor = db.cursor()
    cursor.execute(
        "DELETE FROM empleados WHERE id = %s",
        (empleado_id,)
    )
    db.commit()
    return cursor.rowcount > 0

def actualizar_empleado(db, empleado_id: int, empleado):
    cursor = db.cursor()
    cursor.execute(
        """
        UPDATE empleados
        SET nombre=%s, departamento=%s, puesto=%s, salario=%s
        WHERE id=%s
        """,
        (
            empleado.nombre,
            empleado.departamento,
            empleado.puesto,
            empleado.salario,
            empleado_id
        )
    )
    db.commit()
    return cursor.rowcount > 0