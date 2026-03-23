def crear_venta(db, venta, user_id):

    cursor = db.cursor(dictionary=True)

    try:

        db.start_transaction()

        # 1️⃣ Crear venta
        cursor.execute(
            """
            INSERT INTO sales (customer_id,total,tipo,created_by)
            VALUES (%s,%s,%s,%s)
            """,
            (
                venta.cliente_id,
                venta.total,
                venta.tipo,
                user_id
            )
        )

        sale_id = cursor.lastrowid


        # 2️⃣ Insertar productos
        for item in venta.items:

            subtotal = item.price * item.cantidad

            cursor.execute(
                """
                INSERT INTO sale_items
                (sale_id,product_id,quantity,price,subtotal)
                VALUES (%s,%s,%s,%s,%s)
                """,
                (
                    sale_id,
                    item.id,
                    item.cantidad,
                    item.price,
                    subtotal
                )
            )


            # 3️⃣ Actualizar stock
            cursor.execute(
                """
                UPDATE products
                SET stock = stock - %s
                WHERE id = %s
                """,
                (
                    item.cantidad,
                    item.id
                )
            )


        # 4️⃣ Registrar pago
        cursor.execute(
            """
            INSERT INTO sale_payments
            (sale_id,method,amount)
            VALUES (%s,%s,%s)
            """,
            (
                sale_id,
                "efectivo",
                venta.total
            )
        )


        db.commit()

        return sale_id


    except Exception as e:

        db.rollback()
        raise e

    finally:

        cursor.close()



def listar_ventas(db):
    cursor = db.cursor(dictionary=True)

    cursor.execute("""
        SELECT s.id, s.total, s.tipo, s.customer_id, s.created_by, s.created_at,
               c.name AS customer_name
        FROM sales s
        LEFT JOIN customers c ON s.customer_id = c.id
        ORDER BY s.id DESC
    """)

    ventas = cursor.fetchall()

    for v in ventas:
        cursor.execute("""
            SELECT si.product_id AS id, p.name, si.quantity AS cantidad, si.price
            FROM sale_items si
            JOIN products p ON si.product_id = p.id
            WHERE si.sale_id = %s
        """, (v['id'],))
        v['items'] = cursor.fetchall()

    cursor.close()
    return ventas


def listar_ventas_paginadas(db, page: int, limit: int, search: str):
    cursor = db.cursor(dictionary=True)
    
    offset = (page - 1) * limit
    search_query = f"%{search}%"
    
    # Traer ventas con cliente y usuario que realizó la venta
    cursor.execute("""
        SELECT s.id, s.total, s.tipo, s.customer_id, s.created_by, s.created_at,
               c.name AS customer_name,
               u.nombre AS usuario
        FROM sales s
        LEFT JOIN customers c ON s.customer_id = c.id
        LEFT JOIN usuarios u ON s.created_by = u.id
        WHERE c.name LIKE %s
           OR s.id IN (
               SELECT si.sale_id
               FROM sale_items si
               JOIN products p ON si.product_id = p.id
               WHERE p.name LIKE %s
           )
        ORDER BY s.id DESC
        LIMIT %s OFFSET %s
    """, (search_query, search_query, limit, offset))
    
    ventas = cursor.fetchall()
    
    # Traer los productos de cada venta
    for v in ventas:
        cursor.execute("""
            SELECT si.product_id AS id, p.name, si.quantity AS cantidad, si.price
            FROM sale_items si
            JOIN products p ON si.product_id = p.id
            WHERE si.sale_id = %s
        """, (v['id'],))
        v['items'] = cursor.fetchall()
    
    # Contar total de registros para paginación
    cursor.execute("""
        SELECT COUNT(*) AS total
        FROM sales s
        LEFT JOIN customers c ON s.customer_id = c.id
        LEFT JOIN usuarios u ON s.created_by = u.id
        WHERE c.name LIKE %s
           OR s.id IN (
               SELECT si.sale_id
               FROM sale_items si
               JOIN products p ON si.product_id = p.id
               WHERE p.name LIKE %s
           )
    """, (search_query, search_query))
    
    total = cursor.fetchone()['total']
    cursor.close()
    
    return {
        "ventas": ventas,
        "page": page,
        "limit": limit,
        "total": total
    }