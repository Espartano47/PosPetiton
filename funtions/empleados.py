def obtener_empleados(db):
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM empleados")
    return cursor.fetchall()


def insertar_empleado(db, empleado):
    cursor = db.cursor()
    cursor.execute("""
        INSERT INTO empleados
        (nombre, departamento, puesto, salario, fecha_ingreso, estado)
        VALUES (%s, %s, %s, %s, %s, %s)
    """, (
        empleado.nombre,
        empleado.departamento,
        empleado.puesto,
        empleado.salario,
        empleado.fecha_ingreso,
        empleado.estado
    ))
    db.commit()
    return cursor.lastrowid
