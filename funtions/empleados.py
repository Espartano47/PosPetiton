def obtener_empleados(db):
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM vista_empleados")
    return cursor.fetchall()


def obtener_empleado_por_id(db, empleado_id: int):
    cursor = db.cursor(dictionary=True)
    cursor.execute(
        "SELECT * FROM vista_empleados WHERE id = %s",
        (empleado_id,)
    )
    return cursor.fetchone()

def insertar_empleado(db, empleado, usuario_id, usuario_nombre,empresaId):
    cursor = db.cursor()
    cursor.execute("""
        INSERT INTO empleados
        (identificacion, nombre, apellido, genero, nacimiento, tipoSangre, estadoCivil,bautizado, telefono, celular, correo, Ocupacion, provincia, municipio, sector, direccion, id_categoria, foto, created, createdById, createdByName,empresaId,id_iglesia)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s, %s, %s, %s, %s, %s, %s, NOW(), %s, %s, %s, %s)
    """, (
        empleado["identificacion"],
        empleado["nombre"],
        empleado["apellido"],
        empleado["genero"],
        empleado["nacimiento"],
        empleado["tipoSangre"],
        empleado["estadoCivil"],
        empleado["bautizado"],
        empleado["telefono"],
        empleado["celular"],
        empleado["correo"],
        empleado["Ocupacion"],
        empleado["provincia"],
        empleado["municipio"],
        empleado["sector"],
        empleado["direccion"],
        empleado["id_categoria"],
        empleado["foto"],
        usuario_id,
        usuario_nombre,
        empresaId,
        empleado["iglesia_id"]
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
    cursor.execute("""
    UPDATE empleados
    SET 
        identificacion = %s,
        nombre = %s,
        apellido = %s,
        genero = %s,
        nacimiento = %s,
        tipoSangre = %s,
        estadoCivil = %s,
        bautizado = %s,
        telefono = %s,
        celular = %s,
        correo = %s,
        Ocupacion = %s,
        provincia = %s,
        municipio = %s,
        sector = %s,
        direccion = %s,
        id_categoria = %s,
        id_iglesia = %s

        WHERE id = %s
    """, (
        empleado["identificacion"],
        empleado["nombre"],
        empleado["apellido"],
        empleado["genero"],
        empleado["nacimiento"],
        empleado["tipoSangre"],
        empleado["estadoCivil"],
        empleado["bautizado"],
        empleado["telefono"],
        empleado["celular"],
        empleado["correo"],
        empleado["Ocupacion"],
        empleado["provincia"],
        empleado["municipio"],
        empleado["sector"],
        empleado["direccion"],
        empleado["id_categoria"],
        empleado["id_iglesia"],
        empleado_id 
    ))
    db.commit()
    
    return cursor.rowcount > 0

        # identificacion = %s,
        # nombre = %s,
        # apellido = %s,
        # genero = %s,
        # nacimiento = %s,
        # tipoSangre = %s,
        # estadoCivil = %s,
        # bautizado = %s,
        # telefono = %s,
        # celular = %s,
        # correo = %s,
        # Ocupacion = %s,
        # provincia = %s,
        # municipio = %s,
        # sector = %s,
        # direccion = %s,
        # id_iglesia = %s