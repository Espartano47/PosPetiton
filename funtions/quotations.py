def crear_quotation(db, data: dict):

    cursor = db.cursor()

    cursor.execute(
        """
        INSERT INTO quotations (client_id, total)
        VALUES (%s,%s)
        """,
        (
            data.get("client_id"),
            data["total"]
        )
    )

    quotation_id = cursor.lastrowid

    for item in data["items"]:

        cursor.execute(
            """
            INSERT INTO quotation_items
            (quotation_id, product_id, name, price, quantity, subtotal)
            VALUES (%s,%s,%s,%s,%s,%s)
            """,
            (
                quotation_id,
                item["id"],
                item["name"],
                item["price"],
                item["cantidad"],
                item["price"] * item["cantidad"]
            )
        )

    db.commit()
    cursor.close()

    return quotation_id


def obtener_quotations(db):

    cursor = db.cursor(dictionary=True)

    cursor.execute("""
        SELECT q.*, c.name as client_name
        FROM quotations q
        LEFT JOIN clients c ON c.id = q.client_id
        ORDER BY q.id DESC
    """)

    data = cursor.fetchall()

    cursor.close()

    return data


def obtener_quotation(db, quotation_id: int):

    cursor = db.cursor(dictionary=True)

    cursor.execute(
        "SELECT * FROM quotations WHERE id=%s",
        (quotation_id,)
    )

    quotation = cursor.fetchone()

    if quotation:

        cursor.execute(
            "SELECT * FROM quotation_items WHERE quotation_id=%s",
            (quotation_id,)
        )

        quotation["items"] = cursor.fetchall()

    cursor.close()

    return quotation


def actualizar_quotation(db, quotation_id: int, data: dict):

    cursor = db.cursor()

    cursor.execute(
        """
        UPDATE quotations
        SET client_id=%s, total=%s
        WHERE id=%s
        """,
        (
            data.get("client_id"),
            data["total"],
            quotation_id
        )
    )

    db.commit()
    cursor.close()


def eliminar_quotation(db, quotation_id: int):

    cursor = db.cursor()

    cursor.execute(
        "DELETE FROM quotations WHERE id=%s",
        (quotation_id,)
    )

    db.commit()
    cursor.close()