def crear_movimiento(db, data: dict):
    cursor = db.cursor()
    cursor.execute(
        """
        INSERT INTO inventory_movements
        (product_id, user_id, type, quantity, stock_before, stock_after, reference)
        VALUES (%s,%s,%s,%s,%s,%s,%s)
        """,
        (
            data["product_id"],
            data.get("user_id"),
            data["type"],
            data["quantity"],
            data["stock_before"],
            data["stock_after"],
            data.get("reference")
        )
    )
    db.commit()
    cursor.close()


def obtener_movimientos(db):
    cursor = db.cursor(dictionary=True)

    cursor.execute("""
        SELECT im.*, p.name as product_name
        FROM inventory_movements im
        LEFT JOIN products p ON p.id = im.product_id
        ORDER BY im.id DESC
    """)

    data = cursor.fetchall()
    cursor.close()

    return data


def obtener_movimiento(db, movement_id: int):

    cursor = db.cursor(dictionary=True)

    cursor.execute(
        "SELECT * FROM inventory_movements WHERE id=%s",
        (movement_id,)
    )

    data = cursor.fetchone()

    cursor.close()

    return data


def actualizar_movimiento(db, movement_id: int, data: dict):

    fields = []
    values = []

    for key, value in data.items():
        if value is not None:
            fields.append(f"{key}=%s")
            values.append(value)

    if not fields:
        return

    values.append(movement_id)

    query = f"""
        UPDATE inventory_movements
        SET {', '.join(fields)}
        WHERE id=%s
    """

    cursor = db.cursor()
    cursor.execute(query, tuple(values))
    db.commit()
    cursor.close()


def eliminar_movimiento(db, movement_id: int):

    cursor = db.cursor()

    cursor.execute(
        "DELETE FROM inventory_movements WHERE id=%s",
        (movement_id,)
    )

    db.commit()
    cursor.close()