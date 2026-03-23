from funtions.inventory_movements import crear_movimiento


def crear_compra(db, data: dict):

    cursor = db.cursor(dictionary=True)

    total = 0

    for item in data["items"]:
        total += item["quantity"] * item["cost"]

    # crear compra
    cursor.execute(
        """
        INSERT INTO purchases (supplier_id,user_id,invoice_number,status,total)
        VALUES (%s,%s,%s,%s,%s)
        """,
        (
            data["supplier_id"],
            data.get("user_id"),
            data.get("invoice_number"),
            data["status"],
            total
        )
    )

    purchase_id = cursor.lastrowid

    # insertar items
    for item in data["items"]:

        item_total = item["quantity"] * item["cost"]

        cursor.execute(
            """
            INSERT INTO purchase_items
            (purchase_id,product_id,quantity,cost,total)
            VALUES (%s,%s,%s,%s,%s)
            """,
            (
                purchase_id,
                item["product_id"],
                item["quantity"],
                item["cost"],
                item_total
            )
        )

        # obtener stock actual
        cursor.execute(
            "SELECT stock FROM products WHERE id=%s",
            (item["product_id"],)
        )

        product = cursor.fetchone()

        stock_before = product["stock"]
        stock_after = stock_before + item["quantity"]

        # actualizar inventario
        cursor.execute(
            "UPDATE products SET stock=%s WHERE id=%s",
            (stock_after, item["product_id"])
        )

        # crear movimiento inventario
        crear_movimiento(db, {
            "product_id": item["product_id"],
            "user_id": data.get("user_id"),
            "type": "entrada",
            "quantity": item["quantity"],
            "stock_before": stock_before,
            "stock_after": stock_after,
            "reference": f"Compra #{purchase_id}"
        })

    # si esta pendiente crear cuenta por pagar
    if data["status"] == "pending":

        cursor.execute(
            """
            INSERT INTO accounts_payable
            (purchase_id,supplier_id,amount,balance,status)
            VALUES (%s,%s,%s,%s,'pending')
            """,
            (
                purchase_id,
                data["supplier_id"],
                total,
                total
            )
        )

    db.commit()
    cursor.close()

    return purchase_id



def obtener_compras(db):

    cursor = db.cursor(dictionary=True)

    cursor.execute("""
        SELECT p.*, s.name supplier_name
        FROM purchases p
        LEFT JOIN suppliers s ON s.id = p.supplier_id
        ORDER BY p.id DESC
    """)

    data = cursor.fetchall()

    cursor.close()

    return data